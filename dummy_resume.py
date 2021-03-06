#!/usr/bin/env python3
# title           : My_resume.py
# description     : Useful information about my career
# author          : Wojtek Zygadlo
# email:          : wzygadlo@outlook.com
# phone:          : +1 778 751 3750
# version         : 1.0
# python_version  : 3.6

import education
import work_experiance as work
import skills
import hobby
import time


class Resume:
    def __init__(level="experienced"):
        super()

    def bio(self):
        info = '''Experienced DevOps Engineer with a demonstrated history of working in the financial services industry. 
                  Skilled in MySQL Database, Linux System Administration, TeamCity, Amazon Web Services (AWS), GCP, CI/CD pipelines. 
                  Strong engineering professional with an Engineer's degree focused on Information Technology.'''
        print(info)

    def skills(self):
        skill = input()
        if skill == "Linux":
            print('''RHEL5/6/7, Debian, Ubuntu, SLES 11/12, Archlinux, and many more''')

        elif skill == "Network Skills":
            print('''Switching (VLAN, Link Aggregation), Wireless
                     Load balancing (HAProxy),
                     TCP/IP,
                     Network monitoring and analysing (Wireshark, nmap, Nagios),
                     Server setup (Apache, nginx, SSH, FTP, DHCP, NTP, SMB, NFS, OpenLDAP, VPN, AFP, SSL)'''
                 )

        elif skill == "Programming":
            print("Shell/BASH", "Python")

        elif skill == "Database":
            print('''MySQL,
                     SQL/SQLPlus''')

        elif skill == "Cloud Solutions":
            print('''AWS (EC2, VPC, CloudFormation, Lambda, Route53....),
                     GCP,
                     Docker,
                     Kubernetes/Helm,
                     '''
                 )
        elif skill == "Automation":
            print('''Ansible,
                     Terraform,
                     AWS CloudFormation,
                     GCP Deployment Manager,
                     Python (Fabric/SDK),
                     Hashicorp Vault (security as a service)'''
                 )
        elif skill == "DevOps Tools":
            print('''Teamcity/Jenkins/Travis CI
                     Flyways,
                     GitHub/GitLab,
                     Jfrog Artifactory,
                     ELK / NewRelic / Nagios,
                     SonarQube'''
                 )

    def work_history(self):
        work = input("Work History: ")
        start_time = time.strftime("%m/%Y")
        end_time = time.strftime("%m/%Y")

        if start_time == "10/2020" and end_time == "present":
            work_history = {"PayPal": "Manager (Team Lead), DevOps Cloud Engineer",
                            "Location": "Vancouver, Canada",
                            "Duties": ['''
                                - Providing DevOps best practices.
                                - Performing continuous analysis of emerging concepts in DevOps, Infrastructure Automation, and Enterprise Security and build up the knowledge base.
                                - Define, own, and continuously revise and communicate the DevOps roadmap.
                                - Lead and coordinate the creation and improvement of Continuous Integration and Continuous Delivery environments.
                                - Monitoring risks and managing/escalating issues.
                                - Define and own effective metrics and reporting.
                                - Identify roadblocks, including technical, resourcing, cultural, and knowledge. Propose and execute mitigation strategies.
                                - Own and lead initiatives to define, design, and implement DevOps solutions, including reference architectures and estimates.
                                - Promote DevOps to all stakeholders
                                ''']}
            print(work_history)  
        
        if start_time == "08/2017" and end_time == "10/2020":
            work_history = {"PayPal/Hyperwallet Systems Inc": "DevOps Engineer/Sr Linux Admin",
                            "Location": "Vancouver, Canada",
                            "Duties": ['''
                                - Building IaC for AWS/GCP and traditional VMware environments.
                                - Designing and implementing a self-deploying fully automated cloud stack
                                - Building Pipeline for all stages via TeamCity in AWS/GCP and on Prem 
                                - Building and implementing automated software deployments at all stages.
                                - Deploying application with Green/Blue strategy
                                - implementation of a CI stack via TeamCity, leveraging cloud scaling for parallel builds and automated regression testing per code branch or commit
                                Main technologies responsible for:
                                - AWS
                                - GCP 
                                - RHEL 6 and 7
                                - Java EJB application based on Glassfish/Payara
                                - Hazelcast JMS brokers
                                - MySQL
                                - Nginx, HAProxy, F5
                                - SignalScience 
                                - Travis-CI and TeamCity for continuous integration
                                - APM, logging, and monitoring - ELK, Splunk, New Relic, Nagios
                                ''']}
            print(work_history)        

        elif start_time == "05/2013" and end_time == "07/2017":
            work_history = {"Cisco Systems LTD": "Systems Engineer",
                            "Location": "Southampton, UK",
                            "Duties": ['''
                                - Managing and monitoring all installed systems and infrastructure to ensure the highest level of availability. (Nagios/ELK/Grafana).
                                - Installing, configuring and testing operating systems, application software.
                                - Managing security, upgrade, and deployment projects on-site.
                                - Built and provided high-level E2E, troubleshooting on Windows, Linux Systems.
                                - Overseeing development and maintenance of customers computer systems
                                   in the Broadcasting industry,
                                - Maintain 24/7 availability for responsible systems. (On-call rotation).
                                - Providing CI based on Jenkins solution.
                                - Monitoring and testing application performance to identify potential bottlenecks,
                                   developing solutions, and collaborate with developers
                                   on solution implementation.
                                - Writing and maintaining custom scripts to increase system efficiency
                                   and performance time.
                                - Providing 2nd and 3rd level technical support and troubleshooting
                                   to internal and external clients.
                            ''']}
            print(work_history)

        elif start_time == "02/2011" and end_time == "05/2013":
            work_history = {"Nokia Siemens Network": "Technical Support Engineer",
                            "Location": "Wroclaw, Poland",
                            "Duties": ['''
                                    - Testing (E2E, IoT),
                                    - Trailing activities,
                                    - Providing 24/7 support (on-call rotation),
                                    - Design and implementation of a test environment
                                       based on Linux RedHat servers.,
                                    - Implementing VLAN solution at the customer side
                                       for Femto/Small Cells network.,
                                    - Features verification, testing new features in new SW release.,
                                    - Remote and onsite support for customers all over the world,
                                    - Providing internal training for customer teams regarding NSN Femto Solution,
                                    - Managing and maintenance experience in Core Networks (MSC, SGSN)
                                       during Femto integration at customer sites,
                                    - Tracking problems and solutions based on Resolve BMC Remedy,
                                       JIRA, Service Desk."
                                ''']}
            print(work_history)

        elif start_time == "10/2007" and end_time == "02/2011":
            work_history = {"TECE": "Network Administrator",
                            "Location": "Strzelin, Poland",
                            "Duties": ['''
                                    - Installation, upgrading and maintaining Servers Windows Server 2003 R2,
                                    - Managing Web server (Apache, IIS),
                                    - Linux server administration based on Debian
                                       (DHCP, Proxy server, Samba, IPtables)
                                       Novell SLES (Backup email server based on eDirecotry)
                                       Ubuntu with KVM for virtualisation.,
                                    - Cisco device management (Switches, Routers),
                                    - Configuration routeing table,
                                    - Maintaining VPN connection between TECE headquarter and branch offices,
                                    - Creating websites (PHP, CSS, HTML),
                                    - Database administration of MySQL, MSSQL,
                                    - Helpdesk for 60 peoples in the TECE Poland office.
                                ''']}
            print(work_history)

        elif start_time == "11/2005" and end_time == "10/2007":
            work_history = {"PHOUA SP z o.o.": "Network Administrator",
                            "Locaton": "Wroclaw, Poland",
                            "Duties": ['''
                                    - Managing network infrastructure
                                    - Implementation WLAN access on Cisco devices
                                    - Maintaining Windows systems
                                    - Helpdesk
                                ''']}
            print(work_history)

        elif start_time == "01/2005" and end_time == "09/2005":
            work_history = {"Minimarket Max": "Help Desk",
                            "Location": "Strzelin, Poland",
                            "Duties": "Programming fiscal cash registers."}
            print(work_history)

    def education(self):
        edu = input("Education: ")
        start_time = time.strftime("%m/%Y")

        if start_time == "01/2010":
            education = {"Bachelor of Science": "Computer Systems and Networks",
                         "School Name": "Wroclaw High School of applied computing (WWSIS)",
                         "School Location": "Wroclaw, Poland"}

        elif start_time == "06/2006":
            education = {"Post-secondary school": "IT",
                         "School Name": "Secondary Study IT 'WIEDZA'",
                         "School Location": "Wroclaw, Poland"}

        elif start_time == "06/2004":
            education = {"Post-secondary school": "IT",
                         "School Name": "EZN Electronic Departments",
                         "School Location": "Wroclaw, Poland"}

    def hobby(self):
        while True:
            hobby = input("Do you have a hobby: ")
            if str.lower(hobby) == "y":
                print("Photography, Hiking, Football, Cyber Security, Marial Arts")
