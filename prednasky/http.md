# HTTP

Budeme stavat na IP (to uz mame given) 1969 arpanet  
Vieme si rozposielat packety ale s ziadnymi guarantees

Chceme vymysliet TCP:

- Checksums (a ECC)  
- Retries  
- ACK’s (SACK)  
- Packet numbering  
- Flow control  
  - Reciever posiela available buffer  
- Congestion control  
  - Slow start, Exponential growth, Congestion avoidance, Loss detection, backoff

\-\> HTTP  
  Request \- Response   
Methods, Headers, Body, URL, Query params

* **Step 1 \- The Query:** You type a web address into your browser, which sends a request to a recursive resolver (like an ISP or a public service). \[[1](https://www.cloudflare.com/learning/dns/what-is-dns/), [2](https://www.fortinet.com/resources/cyberglossary/what-is-dns)\]  
* **Step 2 \- Checking the Cache:** The resolver checks its memory to see if it already stored that website's IP address recently. \[[1](https://www.fortinet.com/resources/cyberglossary/what-is-dns), [2](https://www.youtube.com/watch?v=UVR9lhUGAyU)\]  
* **Step 3 \- Root Nameserver:** If the address is not cached, the resolver asks a root nameserver, which points to the correct domain extension. \[[1](https://www.cloudflare.com/learning/dns/what-is-dns/), [2](https://www.fortinet.com/resources/cyberglossary/what-is-dns)\]  
* **Step 4 \- TLD Nameserver:** The resolver queries the Top-Level Domain server (such as `.com` or `.org`), which directs it to the specific domain registry. \[[1](https://www.cloudflare.com/learning/dns/what-is-dns/), [2](https://www.fortinet.com/resources/cyberglossary/what-is-dns)\]  
* **Step 5 \- Authoritative Nameserver:** The resolver asks the authoritative nameserver for that exact website, which provides the final IP address. \[[1](https://www.cloudflare.com/learning/dns/what-is-dns/), [2](https://www.fortinet.com/resources/cyberglossary/what-is-dns)\]  
* **Step 6 \- Delivery:** The resolver hands the IP address back to your device, allowing your browser to load the page as explained in the [Cloudflare DNS Guide](https://www.cloudflare.com/learning/dns/what-is-dns/). \[[1](https://www.fortinet.com/resources/cyberglossary/what-is-dns), [2](https://www.youtube.com/watch?v=UVR9lhUGAyU)\]

**NAT**  
**To vedlo k modelu „hloupé minimální sítě“ s chytrými terminály, který byl úplně odlišný od předchozího modelu chytré sítě s hloupými terminály.** 
