import csv

def analyze_traffic(file):
    packets_sent = 0
    packets_received = 0
    total_data = 0

    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Direction'] == 'Sent':
                packets_sent += 1
                total_data += int(row['Length'])
            elif row['Direction'] == 'Received':
                packets_received += 1

    packet_loss = (packets_sent - packets_received) / packets_sent * 100
    throughput = total_data / 1024  # KB/s
    print(f"Packet Loss: {packet_loss:.2f}%")
    print(f"Throughput: {throughput:.2f} KB/s")

# Example usage
analyze_traffic('traffic.csv')
