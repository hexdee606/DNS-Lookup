#!/usr/bin/python3
"""
#############################################################################
#                               DNS-Lookup                                  #
#############################################################################
# Copyright 2021 Alchemists                                                 #
#############################################################################
# A DNS-Lookup (c) 2021, This work is marked with CC0 1.0 Universal.        #
# To view a copy of this license, visit                                     #
#                                                                           #
# http://creativecommons.org/publicdomain/zero/1.0                          #
#                                                                           #
# Unless required by applicable law or agreed to in writing, software       #
# distributed under the License is distributed on an "AS IS" BASIS,         #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
# See the License for the specific language governing permissions and       #
# limitations under the License.                                            #
#############################################################################
#                               ABOUT Alchemists                            #
#############################################################################
#           |   Github      |   Twitter     |   GMail                       #
############|###############|###############|################################
# Developer |   hexdee606   |   hexdee606   |   hexdee606                   #
#############################################################################
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
        print("|                                       DNS-Lookup                                            |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| Copyright 2021 Alchemists                                                                   |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| A DNS-Lookup (c) 2021, This work is marked with CC0 1.0 Universal.                          |")
        print("| To view a copy of this license, visit                                                       |")
        print("|                                                                                             |")
        print("| http://creativecommons.org/publicdomain/zero/1.0                                            |")
        print("|                                                                                             |")
        print("| Unless required by applicable law or agreed to in writing, software distributed under       |")
        print("| the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY   |")
        print("| KIND, either express or implied. See the License for the specific language governing        |")
        print("| permissions and limitations under the License.                                              |")
        print("|---------------------------------------------------------------------------------------------|")
        print("|                                        ABOUT Alchemists                                     |")
        print("|---------------------------------------------------------------------------------------------|")
        print("|                |      Github       |      Twitter      |      GMail                         |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| Developer      |      hexdee606    |      hexdee606    |      hexdee606                     |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| DNS Lookup (Version 1.1 - Beta)                                                             |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| USE CTRL + C to Exit this code                                                              |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| {:<28} | {:<60} |".format('Total numbers of domains', total_domains))
        print("|---------------------------------------------------------------------------------------------|")
        print("| {:<10} | {:<15} | {:<60} |".format('Sr. Number', 'Resolved Add.', 'Domain name'))
        print("|---------------------------------------------------------------------------------------------|")
        
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("|                                       DNS-Lookup                                            |")
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("| Copyright 2021 Alchemists                                                                   |")
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("| A DNS-Lookup (c) 2021, This work is marked with CC0 1.0 Universal.                          |")
        results.append("| To view a copy of this license, visit                                                       |")
        results.append("|                                                                                             |")
        results.append("| http://creativecommons.org/publicdomain/zero/1.0                                            |")
        results.append("|                                                                                             |")
        results.append("| Unless required by applicable law or agreed to in writing, software distributed under       |")
        results.append("| the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY   |")
        results.append("| KIND, either express or implied. See the License for the specific language governing        |")
        results.append("| permissions and limitations under the License.                                              |")
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("|                                        ABOUT Alchemists                                     |")
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("|                |      Github       |      Twitter      |      GMail                         |")
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("| Developer      |      hexdee606    |      hexdee606    |      hexdee606                     |")
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("| DNS Lookup (Version 1.1 - Beta)                                                             |")
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("| USE CTRL + C to Exit this code                                                              |")
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("| {:<28} | {:<60} |".format('Total numbers of domains', total_domains))
        results.append("|---------------------------------------------------------------------------------------------|")
        results.append("| {:<10} | {:<15} | {:<60} |".format('Sr. Number', 'Resolved Add.', 'Domain name'))
        results.append("|---------------------------------------------------------------------------------------------|")
       

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
    try:
        print("|---------------------------------------------------------------------------------------------|")
        print("|                                       DNS-Lookup                                            |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| Copyright 2021 Alchemists                                                                   |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| A DNS-Lookup (c) 2021, This work is marked with CC0 1.0 Universal.                          |")
        print("| To view a copy of this license, visit                                                       |")
        print("|                                                                                             |")
        print("| http://creativecommons.org/publicdomain/zero/1.0                                            |")
        print("|                                                                                             |")
        print("| Unless required by applicable law or agreed to in writing, software distributed under       |")
        print("| the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY   |")
        print("| KIND, either express or implied. See the License for the specific language governing        |")
        print("| permissions and limitations under the License.                                              |")
        print("|---------------------------------------------------------------------------------------------|")
        print("|                                        ABOUT Alchemists                                     |")
        print("|---------------------------------------------------------------------------------------------|")
        print("|                |      Github       |      Twitter      |      GMail                         |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| Developer      |      hexdee606    |      hexdee606    |      hexdee606                     |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| DNS Lookup (Version 1.1 - Beta)                                                             |")
        print("|---------------------------------------------------------------------------------------------|")
        print("| USE CTRL + C to Exit this code                                                              |")
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
        
    except KeyboardInterrupt:
        print("|---------------------------------------------------------------------------------------------|")
        print("| {:<91} |".format('Process cancelled by user.'))
        print("|---------------------------------------------------------------------------------------------|")
    finally:
        pass
