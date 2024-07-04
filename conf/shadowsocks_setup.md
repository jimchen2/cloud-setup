```bash
sudo apt update
sudo apt install shadowsocks-libev
```
```bash
root@localhost:/etc/shadowsocks-libev# cat config.json 
{
  "server": ["::", "0.0.0.0"],
  "server_port": 8388,
  "password": "*************",
  "timeout": 300,
  "method": "chacha20-ietf-poly1305",
  "mode": "tcp_and_udp",
  "fast_open": true,
  "nameserver": "2606:4700:4700::1113,2606:4700:4700::1003"
}
```

########### clash.yml #####################
proxies:
  - name: "Shadowsocks"
    type: ss
    server: 172.235.48.74
    port: 8388
    cipher: chacha20-ietf-poly1305
    password: "*************"

dns:
  enable: true
  ipv6: true
  nameserver:
    - https://family.cloudflare-dns.com/dns-query
  fallback:
    - tls://family.cloudflare-dns.com:853
    - 2606:4700:4700::1113
    - 2606:4700:4700::1003
    
    