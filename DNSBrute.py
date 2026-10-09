#! /usr/bin/python3

import argparse
import socket
import json
import sys
import os

# Colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def banner():
    print(f"""
    {CYAN}{BOLD}
╭──────────────────────────────────────────╮
│              DNSBRUTE v1.0               │
╰──────────────────────────────────────────╯
    {RESET}""")

def dnsbrute(domain, wordlist, outputfile):
    # Read the wordlist file
    try:
        with open(wordlist, "r") as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except Exception as reading_wordlist_error:
        print(f"{RED}[!] Failed to read the wordlist: {reading_wordlist_error}\n{RESET}")
        sys.exit(1)

    print(f"  Target    : {domain}")
    print(f"  Wordlist  : {wordlist}")
    print(f"  Entries   : {len(subdomains)}")
    print()

    print(f"{CYAN}[•] Starting DNS enumeration...{RESET}\n")
    results = []

    # Resolver
    for sub in subdomains:
        hostname = f"{sub}.{domain}"
        try:
            ipaddr = socket.gethostbyname(hostname)
            result = {
                "hostname": hostname,
                "ipaddress": ipaddr
            }
            results.append(result)
            print(f"[+] {hostname:<30} → {GREEN}{ipaddr}{RESET}")
        except socket.gaierror:
            pass

    # Save results as JSON
    try:
        with open(outputfile, "w") as output:
            json.dump(results, output, indent=4)
    except OSError as saving_result_error:
        print(f"{RED}[!] Failed to save JSON: {saving_result_error}\n{RESET}")
        sys.exit(1)

    # Print output
    print()
    print("─" * 48)
    print(f"{BOLD}  Results{RESET}")
    print("─" * 48)
    print(f"  Checked   : {len(subdomains)}")
    print(f"  Found     : {len(results)}")
    print(f"  Saved to  : {outputfile}")
    print()

# Check whether the wordlist file exists and is not empty
def wordlist_validation(wordlist):
    if not os.path.isfile(wordlist):
        print(f"{RED}[!] {wordlist}: No such a file\n{RESET}")
        sys.exit(1)

    if os.path.getsize(wordlist) == 0:
        print(f"{RED}[!] {wordlist} file doesn't contain any content!\n{RESET}")
        sys.exit(1)

def main():
    # Create an argument parser
    # ArgumentDefaultsHelpFormatter ensures default values are shown in the help text
    parser = argparse.ArgumentParser(description="Simple DNS subdomain enumerator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Define the command-line arguments
    parser.add_argument("-d", "--domain", metavar='', default="example.com", help="Domain to enumerate")
    parser.add_argument("-w", "--wordlist", metavar='', default="dns_wordlist.txt", help="Path to subdomain wordlist")
    parser.add_argument("-o", "--outputfile", metavar='', default="dnsbrute.json", help="Path to save the output")

    # Parse and use the arguments
    args = parser.parse_args()

    # Show banner
    banner()

    # Validate the wordlist file
    wordlist_validation(args.wordlist)

    # DNS bruteforce
    dnsbrute(args.domain, args.wordlist, args.outputfile)


main()