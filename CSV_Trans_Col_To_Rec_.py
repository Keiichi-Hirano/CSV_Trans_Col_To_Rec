#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#! /usr/bin/env python
# csvファイル読み込みライブラリをImport
import os
import csv

def trance(I_files,O_files,begin,column,repeat):
#+---------+---------+---------                
# I_files :     入力ファイル名（Fullpath)
# O_files :     出力ファイル名（Fullpath)
# keys :        行に展開しない列項目数（粒度やキーとしての役割）
# degin :       開始は0列になるので13列目なら12
# column :      7列分を移動するなら7
# repeat :      列→行変換を繰り返す回数
#+---------+---------+---------                
#       入力ファイルを文字コードutf8で開く
        f = open(I_files, 'r',encoding="utf-8_sig")
        reader = csv.reader(f)
#       出力ファイルを文字コードutf8で開く
        fo = open(O_files, 'w',encoding="utf-8_sig")
        writer = csv.writer(fo, lineterminator='\n')
#       入力ファイルを読み込み、レコード分繰り返し
        for i, row in enumerate(reader):
#               最初のレコードをHeaderとして処理
                if i == 0:
                        #Hearder 編集
                        new = row[0:begin+column]
                        writer.writerow(new)
                        continue                        
#+---------+---------+---------                
#               以降、データレコードとしての処理を実施
#+---------+---------+---------
#               beginに列を行へ移動する開始位置を設定
                start = begin
#               移動する列項目数を設定
#               列→行変換を指定回数分実施する。
                for _ in range(repeat):
#               start列目からColumn列分をrange回数分繰り返して
#               列を行に変換して出力する。       
                        writeing(writer,new,row,start,column,begin)
                        start += column
#                       回数指定が項目列を超過した場合は該当のレコード編集は終わり
                        if start >= len(row):
                                break
        f.close()
        fo.close()

def writeing(writer,new,row,start,column,begin):
#+---------+---------+---------                
# 開始位置(start)、列数(column)をもとにレコード(row)から
# 列のデータを取得し、先頭列（row[0:begin]）と併せて
# 出力ファイル(writer)に出力を行う
#+---------+---------+---------                
        end = start + column
        new = row[0:begin]
        new.extend(row[start:end])
        writer.writerow(new)

def main():
# I_file = "C:/Users/js0059/OneDrive - Coca-Cola Bottlers Japan/ドキュメント/APRILtest.csv"
# O_file = 'C:/Users/js0059/OneDrive - Coca-Cola Bottlers Japan/ドキュメント/APRILtest_output.csv'
# trance(I_file,O_file)

 I_file = "C:/TransFiles/input.csv"
 O_file = 'C:/TransFiles/output.csv'
# 先頭19項目(変換しない項目数12+移動7)の列構成で、12(13-1)列以降7項目単位に5回、列→行変換を行う
 trance(I_file,O_file,12,7,5)

if __name__ == '__main__':
        main()
