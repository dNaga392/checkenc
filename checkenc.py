# -*- coding: utf-8 -*-
import glob


def get_file_encoding(filename: str) -> str:
    lookup = ('utf-8', 'utf_8',
              'euc_jp', 'euc_jis_2004', 'euc_jisx0213',
              'cp932',
              'shift_jis', 'shift_jis_2004', 'shift_jisx0213',
              'iso2022jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_3',
              'iso2022_jp_ext', 'latin_1', 'ascii')
    for encoding in lookup:
        try:
            fp = open(filename, 'r', encoding=encoding)
            fp.read()
            return encoding
        except:
            pass
        finally:
            fp.close()

    return 'unknown'


def print_file_encoding(filename: str) -> None:
    print('[' + get_file_encoding(filename) + '] : ' + filename)


if __name__ == "__main__":
    files = []
    exts = ['h', 'cpp']
    for ext in exts:
        # スクリプト配置フォルダのファイル一覧取得
        files.extend(glob.glob("*." + ext))
    # エクスプローラ同様に名前順にする
    files.sort()
    for filename in files:
        print_file_encoding(filename)
