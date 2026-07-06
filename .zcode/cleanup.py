import os
for p in ['nowcoder_data/21049_Kafka.json', 'nowcoder_data/580_链表.json', 'nowcoder_data/kafka_test.log',
          'nowcoder_data/output/Kafka.md', 'nowcoder_data/output/链表.md']:
    full = os.path.join(r'D:/Workspace/Project/cs-interview', p)
    if os.path.exists(full):
        os.remove(full)
        print(f'removed {p}')
print('done')
