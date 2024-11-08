import time

start = time.perf_counter()

stdin = open('tuesday_json_file.json', 'r')
stdout = open('tuesday_schedule_yaml.yaml', 'w')
stdin_1 = open('friday_json_file.json', 'r')
stdout_1 = open('friday_schedule_yaml.yaml', 'w')

def f(file):
    text = file.read()
    ans_yaml = ""
    line = text.split('\n')
    for i in range(1, len(line) - 1):
        left = 0
        right = 0
        counter = line[i].count('\t')
        for j in range(len(line[i])):
            if left == 0 and line[i][j] == '"':
                left = j + 1
            elif left != 0 and line[i][j] == '"':
                right = j
        ans = line[i][left:right]
        ans = ans.replace('"', '')

        #print(ans)

        if len(ans) != 0:
            if ',' in line[i - 1]:
                if "_teacher" in ans or "_place" in ans or "_tipe" in ans or "_lesson" in ans:
                    ans_yaml += (counter - 2) * '  ' + ans + "\n"
                else:
                    ans_yaml += (counter - 1) * '  ' + ans + "\n"
            elif '},' in line[i - 2] and '{' in line[i - 1]:
                ans_yaml += (counter - 3) * '  ' + '- ' + ans + "\n"
            elif '[' in line[i - 2]:
                ans_yaml += (counter - 3) * '  ' + '- ' + ans + "\n"
            elif '{' in line[i - 1]:
                ans_yaml += (counter - 1) * '  ' + ans + ':\n'
    return ans_yaml


stdout.write(f(stdin))
stdout.close()
stdin.close()

stdout_1.write(f(stdin_1))
stdout_1.close()
stdin_1.close()

print(time.perf_counter() - start)
