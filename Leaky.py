incoming = [1, 4, 3, 0, 5]
bucket_size = 5
leak_rate = 2
bucket = 0

print("Time\tIncoming\tBucket\tSent\tDropped")

for t in range(len(incoming)):
    packets = incoming[t]
    bucket += packets
    dropped = 0
    if bucket > bucket_size:
        dropped = bucket - bucket_size
        bucket = bucket_size
    sent = min(bucket, leak_rate)
    bucket -= sent
    print(f"{t+1}\t{packets}\t\t{bucket}\t{sent}\t{dropped}")
