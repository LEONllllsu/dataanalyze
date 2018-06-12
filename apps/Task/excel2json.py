# _*_ coding: utf-8 _*_
__author__ = 'leonsu'
__date__ = '2018/5/25 13:56'
import xlrd
import json
import codecs
import os


def readExcel(file_floder, filename, user, task_id):
    excel = xlrd.open_workbook(filename)

    sheet = excel.sheet_names()
    for i in range(0, len(sheet)):
        sheettemp = excel.sheets()[i]
        nrows = sheettemp.nrows
        ncols = sheettemp.ncols

        totalArray = []
        tittle = []

        for n in range(0, ncols):
            tittle.append(sheettemp.cell(0, n).value)

        for rowindex in range(1, nrows):
            dic = {}
            for colindex in range(0, ncols):
                s = sheettemp.cell(rowindex, colindex).value
                dic[tittle[colindex]] = s
            totalArray.append(dic)

        json_data = json.dumps(totalArray, ensure_ascii=False)
        output = open(file_floder+str(user)+'-'+str(task_id)+'-step1.json', 'w+')
        output.write(json_data)