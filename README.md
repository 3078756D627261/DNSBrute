# 🔎 DNSBRUTE - Python-Based DNS Subdomain Enumerator

[![GitHub](https://img.shields.io/badge/github-repo-3776AB?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OS](https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black")](https://img.shields.io/)
[![LAB](https://img.shields.io/badge/Security-Lab-8A2BE2?style=for-the-badge)]("https://github.com/3078756D627261/DNSBrute/")

A lightweight command-line tool for discovering `subdomains` through `DNS resolution`. Built with `Python` for learning, experimentation, and authorized security testing.

---

## ⚠️ Disclaimer
> [!WARNING]
> This project was created for educational purposes to explore Python programming, DNS resolution, command-line interfaces, and basic reconnaissance techniques.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 Subdomain Enumeration | Checks potential subdomains using a wordlist |
| 🌐 DNS Resolution | Uses Python's built-in `socket` module to resolve hostnames |
| 🎨 Colored Terminal Output | Displays results with ANSI colors |
| 📄 JSON Export | Saves discovered hostnames and IP addresses in JSON format |
| ⚙️ Command-Line Arguments | Customize the target domain, wordlist, and output file |
| 🛡️ Input Validation | Checks whether the wordlist exists and is not empty |
| 📦 Zero Third-Party Dependencies | Uses Python's standard library |

---

## 📌 Overview

**DNSBRUTE** is a simple Python tool that performs DNS-based `subdomain enumeration` using a `custom wordlist`. It takes a target domain, generates potential subdomains from the provided wordlist, and attempts to resolve each `hostname` to an `IPv4 address`. Successfully resolved hostnames and their corresponding IP addresses are displayed in the terminal and saved to a `JSON` file.

---

## 📂 Project Structure

A typical project layout looks like this:

```text
DNSBRUTE/
│
├── dnsbrute.py       # Main Python script
├── dns_wordlist.txt  # Subdomain wordlist
├── dnsbrute.json     # Generated results
└── README.md         # Project documentation
```

The JSON output file is generated when the script runs successfully.

---

## ⚙️ How It Works

`DNSBRUTE` follows a straightforward enumeration process:

1. **Load the wordlist:** Reads potential subdomain names from a text file.
2. **Generate hostnames:** Combines each wordlist entry with the target domain.
3. **Resolve DNS:** Attempts to resolve each generated hostname using `socket.gethostbyname()`.
4. **Collect results:** Stores successfully resolved hostnames and IPv4 addresses.
5. **Export results:** Saves the collected data to a JSON file.
6. **Display summary:** Prints the number of candidates checked, successful resolutions, and output file location.

### Example

Given the target domain:

```text
example.com
```

And a wordlist containing:

```text
www
mail
ftp
dev
blog
```

DNSBRUTE generates the following candidate hostnames:

```text
www.example.com
mail.example.com
ftp.example.com
dev.example.com
blog.example.com
```

Each hostname is checked through `DNS resolution`.

Only successfully resolved hostnames are included in the results.

> [!IMPORTANT]
> DNS resolution alone does not prove that a hostname is an active website or a separate server. Multiple hostnames may resolve to the same IP address.

---

## 📋 Requirements

- Python 3.x
- A text file containing potential subdomain names
- Network connectivity and access to a working DNS resolver

No external Python packages are required.

## 🚀 Installation

### 1. Clone the repository

```text
git clone https://github.com/3078756D627261/DNSBrute.git
```

### 2. Navigate to the project directory

```text
cd DNSBRUTE
```

### 3. Prepare your wordlist

Create a file named `dns_wordlist.txt` in the project directory.

Example:

```text
www
mail
ftp
dev
test
blog
api
admin
shop
```

Each line should contain one potential subdomain label.

You can also use an existing wordlist that you are authorized to use.

### 4. Run DNSBRUTE

```text
python3 dnsbrute.py
```

By default, `DNSBRUTE` uses:

| Option | Default value |
|---|---|
| Target domain	| example.com |
| Wordlist | dns_wordlist.txt |
| Output file |	dnsbrute.json |

---

## 💻 Usage

`DNSBRUTE` supports three command-line arguments.

Command-line options:

| Argument | Description | Default |
|---|---|---|
| -d, --domain | Target domain to enumerate | example.com |
| -w, --wordlist | Path to the subdomain wordlist | dns_wordlist.txt |
| -o, --outputfile | Path to the JSON output file | dnsbrute.json |
| -h, --help | Display help information | - |

1. Basic usage

Run the tool with its default arguments:

```text
python3 dnsbrute.py
```

2. Specify a target domain

```text
python3 dnsbrute.py -d example.com
```

Or use the long argument:

```text
python3 dnsbrute.py --domain example.com
```

3. Specify a custom wordlist

```text
python3 dnsbrute.py -d example.com -w my_wordlist.txt
```

4. Specify an output file

```text
python3 dnsbrute.py -d example.com -w dns_wordlist.txt -o results.json
```

5. Use all arguments

```text
python3 dnsbrute.py --domain example.com --wordlist dns_wordlist.txt --outputfile results.json
```

6. Display help

```text
python3 dnsbrute.py --help
```

---

## 🖥️ Example Output

The following is an `illustrative example`. Actual results depend on DNS records and network conditions.

```text
╭──────────────────────────────────────────╮
│              DNSBRUTE v1.0               │
╰──────────────────────────────────────────╯

  Target    : example.com
  Wordlist  : dns_wordlist.txt
  Entries   : 10

[•] Starting DNS enumeration...

[+] www.example.com               → 192.0.2.10
[+] mail.example.com              → 192.0.2.20
[+] dev.example.com               → 192.0.2.30

────────────────────────────────────────────────
  Results
────────────────────────────────────────────────
  Checked   : 10
  Found     : 3
  Saved to  : dnsbrute.json
```

> [!IMPORTANT]
> The IP addresses above are reserved for documentation and are not intended to represent actual DNS results.

### JSON Output

`DNSBRUTE` stores discovered `hostnames` and their `IPv4 addresses` in a `JSON` array.

Example:

```text
{
    {
        "hostname": "www.example.com",
        "ipaddress": "192.0.2.10"
    },
    {
        "hostname": "mail.example.com",
        "ipaddress": "192.0.2.20"
    },
    {
        "hostname": "dev.example.com",
        "ipaddress": "192.0.2.30"
    }
}
```

Each object contains two fields:

| Field	| Description |
|---|---|
| hostname | The successfully resolved hostname |
| ipaddress | The IPv4 address returned by DNS resolution |

The output can be used for further analysis or imported into other scripts.

---

## 🧠 Technical Details

`DNSBRUTE` uses several Python standard-library modules.

| Module | Purpose |
|---|---|
| argparse | Parses command-line arguments |
| socket | Resolves hostnames to IPv4 addresses |
| json | Exports results in JSON format |
| sys | Exits when certain errors occur |
| os | Validates the wordlist file |

### DNS Resolution

The script uses:

```text
socket.gethostbyname(hostname)
```

This function attempts to resolve a hostname to an IPv4 address.

If resolution fails with `socket.gaierror`, the script skips that candidate and continues.

### Wordlist Validation

Before enumeration, DNSBRUTE checks whether the specified wordlist:

```text
- Exists as a file
- Is not empty
```

If either check fails, the program displays an error and exits.

### Result Export

Results are written using:

```text
json.dump(results, output, indent=4)
```

The indentation makes the generated JSON file easier to read.

---

## ⚠️ Limitations

DNSBRUTE is intentionally simple and has several limitations:

- **IPv4 only**: Uses `socket.gethostbyname()`, which returns an IPv4 address.
- **Sequential execution**: Checks candidates one at a time.
- **No wildcard detection**: May report misleading results for domains configured with wildcard DNS records.
- **No DNS record selection**: Does not explicitly query record types such as `A`, `AAAA`, `MX`, or `TXT`.
- **Basic error handling**: Skips failed DNS resolutions without displaying individual errors.
- **Resolver-dependent results**: Results may vary with `DNS caching`, `resolver configuration`, and `network conditions`.
- **No HTTP verification**: Does not check whether discovered hostnames serve websites.

These limitations make the project suitable as a `starting point` for learning about `DNS enumeration`.

---

## 🛡️ Ethical Use

`DNSBRUTE` is intended for educational purposes and authorized security testing.

Please follow these guidelines:

```text
✅ Test domains you own or have explicit permission to assess.
✅ Use the tool to learn about DNS, Python, and security fundamentals.
✅ Respect organizational policies and applicable laws.
❌ Do not use the tool for unauthorized reconnaissance.
```
