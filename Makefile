.PHONY: install lint check clean

install:
	bash install.sh

lint:
	shellcheck bin/m4zk1p lib/platform.sh install.sh uninstall.sh || true
	python3 -m py_compile lib/payload.py lib/otp.py
	node --check lib/auto.js

check: lint
	@echo "sintaks bersih"

clean:
	rm -rf node_modules lib/auth lib/*.tmp __pycache__ lib/__pycache__
