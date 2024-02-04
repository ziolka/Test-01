from collections import Counter


def get_count_visits_from_ip(ips):
    print(f'Count {ips}')
    ip_counts = Counter(ips)
    print(ip_counts)
    return ip_counts
    

def get_frequent_visit_from_ip(ips):
    print(f'Frequent: {ips}')
    ip_counts = Counter(ips)
    frequent_ip = ip_counts.most_common(1)
    print(frequent_ip)
    frequent_ip_tuple = frequent_ip[0]
    print(frequent_ip_tuple)
    return frequent_ip_tuple