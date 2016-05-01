import sys
import dns

query = sys.argv[1]

reqobj = dns.Request()
answerobj = reqobj.req(name = query, qtype = dns.Type.ANY)
if not len(answerobj.answers):
    print("Not found.")
for item in answerobj.answers:
    print("%-5s %s" % (item['typename'], item['data']))
