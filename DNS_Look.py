"""

"""
import sys
from os import name, system

try:
    import dns.resolver
except ImportError:
    print('Please install dnspython from internet.')
    sys.exit()


def resolve_dns(dns_server, path_of_domain_name_list):
    try:

        resolver = dns.resolver.Resolver()  # Call resolver as dns.resolver.Resolver() to resolve domain address
        resolver.nameservers = [dns_server]  # Set Domain Name Server as per user input
        file = open(path_of_domain_name_list)  # Open Domain Name List File
        content = file.read()  # Read Domain Names and Store in Content
        domain_name_list = content.splitlines()  # split domain names and store in domain_name_list
        total_domains = 0  # to count total_domains in file
        total_resolved_domain = 0  # to count total number of resolved domains
        results = []
        # Count total number of domains available in file
        for x in domain_name_list:
            total_domains += 1

        # print out put message
        print("|---------------------------------------------------------------------------------------------|")
        print("| DNS Lookup (Version 1.0 - Beta)                                                             |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| USE CTRL + C to Exit this code                                                              |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| {:<28} | {:<60} |".format('Total numbers of domains', total_domains))
        print("|---------------------------------------------------------------------------------------------|")
        print("| {:<10} | {:<15} | {:<60} |".format('Sr. Number', 'Resolved Add.', 'Domain name'))
        print("|---------------------------------------------------------------------------------------------|")

        results.append("|---------------------------------------------------------------------------------------------|"
                       )
        results.append("| DNS Lookup (Version 1.0 - Beta)                                                             |"
                       )
        results.append("|---------------------------------------------------------------------------------------------|"
                       )
        results.append("| USE CTRL + C to Exit this code                                                              |"
                       )
        results.append("|---------------------------------------------------------------------------------------------|"
                       )
        results.append("| {:<28} | {:<60} |".format('Total numbers of domains', total_domains))
        results.append("|---------------------------------------------------------------------------------------------|"
                       )
        results.append("| {:<10} | {:<15} | {:<60} |".format('Sr. Number', 'Resolved Add.', 'Domain name'))
        results.append("|---------------------------------------------------------------------------------------------|"
                       )

        # Push request to dns to resolve domain name
        for domain_name in domain_name_list:
            total_resolved_domain += 1
            try:
                for dns_ip in resolver.resolve(domain_name):
                    print("| {:<10} | {:<15} | {:<60} |".format(total_resolved_domain, dns_ip.to_text(), domain_name))
                    results.append("| {:<10} | {:<15} | {:<60} |".format(total_resolved_domain, dns_ip.to_text(),
                                                                         domain_name))
            except:
                print("| {:<10} | {:<15} | {:<60} |".format(total_resolved_domain, " NOT RESOLVED", domain_name))
                results.append("| {:<10} | {:<15} | {:<60} |".format(total_resolved_domain, " NOT RESOLVED",
                                                                     domain_name))
                pass
            print("|---------------------------------------------------------------------------------------------|")
            results.append("|------------------------------------------------------------------------------------"
                           "---------|")
            with open("DNS_LOOKUP_RESULTS.txt", "w") as f:
                for result in results:
                    print(result, file=f)
    except KeyboardInterrupt:
        print("|---------------------------------------------------------------------------------------------|")
        print("| {:<91} |".format('Process cancelled by user.'))
        print("|---------------------------------------------------------------------------------------------|")

        results.append("|------------------------------------------------------------------------------------"
                       "---------|")
        results.append("| {:<91} |".format('Process cancelled by user.'))
        results.append("|-------------------------------------------------------------------------------------"
                       "--------|")

        with open("DNS_LOOKUP_RESULTS.txt", "w") as f:
            for result in results:
                print(result, file=f)
    finally:
        pass


if __name__ == '__main__':
    print("|---------------------------------------------------------------------------------------------|")
    print("| DNS Lookup (Version 1.0 - Beta)                                                             |")
    print("|---------------------------------------------------------------------------------------------|")
    print("| Please enter following details:                                                             |")
    print("|---------------------------------------------------------------------------------------------|")
    user_input_dns_server = input('Enter Domain Name Server (DNS)\t:\t')
    print("|---------------------------------------------------------------------------------------------|")
    user_input_domain_name_list = input('Enter path of domain name list (Ex. \'\\user\\domain.txt\')\t:\t')
    print("|---------------------------------------------------------------------------------------------|")

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

    resolve_dns(user_input_dns_server, user_input_domain_name_list)
