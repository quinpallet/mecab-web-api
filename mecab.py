import subprocess
from subprocess import PIPE
import traceback

import MeCab
import unidic


# Get dictionary path and name
def get_dicdir(dic_id: str = '') -> tuple:
    dicdir = ''
    dicname = 'mecab'

    try:
        if dic_id == 'unidic':
            dicdir = unidic.DICDIR
            dicname = 'mecab-unidic-neologd'
        elif dic_id == 'ipadic':
            # neologd dictionary path
            proc = subprocess.run('echo `mecab-config --dicdir`"/mecab-ipadic-neologd"', shell=True, stdout=PIPE, stderr=PIPE, text=True)
            dicdir = proc.stdout.strip()
            dicname = 'mecab-ipadic-neologd'
        else:
            # mecab default dictionary path
            proc = subprocess.run('mecab -D | grep filename', shell=True, stdout=PIPE, stderr=PIPE, text=True)
            dicdir = proc.stdout.strip().split('\t')[1][:-8]  # except dic filename 'sys.dic'
    except Exception:
        traceback.print_exc()

    return dicdir, dicname


# Morphological analysis using MeCab
def mecab_parser(text: str, params: dict = {}) -> tuple:
    # MeCab parameters
    cmd_params = []
    # output format
    output_format = 'none'
    # dictionary
    use_dic = 'mecab'
    # parsing result
    result = []

    # checking parameters
    try:
        if 'O' in params:
            cmd_params.append(f'-O{params["O"]}')
            output_format = params['O']
        if 'd' in params:
            # assume 'unidic' or 'ipadic' for parameter 'd'
            dicdir, use_dic = get_dicdir(params['d'])
            if dicdir != '':
                cmd_params.append(f'-d {dicdir}')
        else:
            # default dictionary, with no parameter 'd'
            dicdir, _ = get_dicdir()
            cmd_params.append(f'-d {dicdir}')
    except Exception:
        traceback.print_exc()
        return output_format, use_dic, result

    # creating MeCab instance with parameters
    try:
        tagger = MeCab.Tagger(' '.join(cmd_params))
    except Exception:
        traceback.print_exc()
        return output_format, use_dic, result

    # reconstruct the analysis result of MeCab
    if 'O' in params:
        # assume 'wakati' for parameter 'O'
        result = tagger.parse(text).strip().split(' ')
    else:
        # reconstruct data according to the props of MeCab analysis results
        props = ['表層形', '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用型', '活用形', '原形', '読み', '発音']
        result = [dict(zip(props, (lambda x: [x[0]] + x[1].split(','))(s.split('\t')))) for s in tagger.parse(text).split('\n')[:-2]]

    return output_format, use_dic, result


if __name__ == '__main__':
    # mecab
    print('default ->', mecab_parser('約束のネバーランド'))
    # mecab -d dictionary-path-to-unidic
    print('unidic ->', mecab_parser('約束のネバーランド', {'d': 'unidic'}))
    # mecab -d dictionary-path-to-ipadic
    print('ipadic ->', mecab_parser('約束のネバーランド', {'d': 'ipadic'}))
