#!/usr/bin/env node
/* Engine Baileys — login QR sekali, lalu kirim tanpa sentuh. */
const fs = require("fs");
const { default: makeWASocket, useMultiFileAuthState, DisconnectReason } =
  require("@whiskeysockets/baileys");
const QR = require("qrcode-terminal");
const pino = require("pino");

const num = process.argv[2].replace(/\D/g, "");
const file = process.argv[3];
const count = Number(process.argv[4]) || 1;
const gap = Number(process.argv[5]) || 1500;
const text = fs.readFileSync(file, "utf8");
const jid = num + "@s.whatsapp.net";

(async () => {
  const { state, saveCreds } = await useMultiFileAuthState(__dirname + "/auth");
  const sock = makeWASocket({
    auth: state,
    logger: pino({ level: "silent" }),
    browser: ["M4zk1pL4y", "Chrome", "1.0"],
  });
  sock.ev.on("creds.update", saveCreds);
  sock.ev.on("connection.update", async (c) => {
    if (c.qr) QR.generate(c.qr, { small: true });
    if (c.connection === "open") {
      for (let i = 1; i <= count; i++) {
        try {
          await sock.sendMessage(jid, { text });
          console.log(`[${i}/${count}] OK`);
        } catch (e) {
          console.log(`[${i}/${count}] GAGAL ${e.message}`);
        }
        if (i < count) await new Promise((r) => setTimeout(r, gap));
      }
      await new Promise((r) => setTimeout(r, 1200));
      sock.end(undefined);
      process.exit(0);
    }
    if (c.connection === "close" &&
        c.lastDisconnect?.error?.output?.statusCode === DisconnectReason.loggedOut) {
      console.log("LOGGED OUT — hapus lib/auth lalu login ulang");
      process.exit(1);
    }
  });
})();
