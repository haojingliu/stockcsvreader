import csv

with open('stock.csv', mode='r') as infile:
    reader = csv.reader(infile)
    table = 'stock'
    with open('stock.sql', mode='w') as outfile:
        outfile.write('''
    create table stock(
        confirm_no int,
        order_no varchar(100),
        trade_date varchar(20),
        `type` varchar(2),
        security varchar(10),
        `unit` int,
        avg_price float(20,4),
        brokerage float(20,4),
        net_proceeds float(20,4),
        settlement_date varchar(120),
        confirmation_status varchar(10)
    );
        ''');
        # Skip title.
        rows = iter(reader)
        next(rows)

        for row in rows:
            query = 'insert into ' + table + ' values ('+ ','.join('"{0}"'.format(w) for w in row[0:-1])+');\n'
            outfile.write(query)
