# reconweb.py
import requests

def scan(url):
    payloads = ["' OR '1'='1", "<script>alert(1)</script>", "../../etc/passwd"]
    for payload in payloads:
        r = requests.get(url + payload)
        if r.status_code == 200 and payload in r.text:
            print(f"[!] Vulnerabilidade possível: {payload}")
        else:
            print(f"[+] Testado: {payload}")

if __name__ == "__main__":
    target = input("Digite a URL alvo: ")
    scan(target)
