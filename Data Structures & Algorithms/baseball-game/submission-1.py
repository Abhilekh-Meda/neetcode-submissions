class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == '+':
                sum_prev_two = record[-1] + record[-2]
                record.append(sum_prev_two)
            elif operation == 'D':
                record.append(record[-1] * 2)
            elif operation == 'C':
                record.pop()
            else: 
                record.append(int(operation))
        return sum(record)