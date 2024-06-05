# Caroline E Dale, Rohan Takhar, et al., 2024.

import sys, csv, re

codes = [{"code":"0208020V0AAADAD","system":"bnf"},{"code":"0208020H0BBAAAA","system":"bnf"},{"code":"0208020V0AAACAC","system":"bnf"},{"code":"0208020V0AAAAAA","system":"bnf"},{"code":"0208020H0AAAAAA","system":"bnf"},{"code":"0208020V0BDAAAC","system":"bnf"},{"code":"0208020S0AAAAAA","system":"bnf"},{"code":"0208020V0AAABAB","system":"bnf"},{"code":"0208020S0BBAAAA","system":"bnf"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('warfarin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["warfarin-tablet---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["warfarin-tablet---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["warfarin-tablet---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
