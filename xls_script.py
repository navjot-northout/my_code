def generate_msg_xls(self):
    import xlwt
    import msg_const
    font_style = xlwt.XFStyle()
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('all_msg')

    all_cont = dir(msg_const)
    for index, var in enumerate(all_cont):
        print (index)
        print (var)

        if var.startswith('_'):
            continue
        ws.write(index, 0, var, font_style)
        ws.write(index, 1, getattr(msg_const, var), font_style)

    wb.save('/home/northout/Desktop/all_msg.xls')