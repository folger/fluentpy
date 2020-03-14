import os
import json
import requests

def main():
    r = requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1')

    V_P = '<script type="application/json" id="captain-config">'
    V_P1 = '</script>'

    p = r.text.find(V_P)
    p1 = r.text.find(V_P1, p)
    # with open('a.html', 'w') as f:
        # f.write(r.text)
    def pr(s):
        print(s)
    conf = json.loads(r.text[p+len(V_P):p1])
    pr(f'[{conf["page"]["title"]}]')
    pr('*' * 20)
    component = conf['component'][0]
    pr(f'{component["title"]} ({component["mapLastUpdatedTime"]})')
    pr('=' * 20)
    def get_value(case, k):
        s = case.get(k, '')
        return s if s else '0'
    def report(place, case):
        def np(k):
            return get_value(case, k)
        items = (f'{place} --',
                f'新增确诊: {np("confirmedRelative")}',
                f'确诊: {np("confirmed")}',
                f'新增治愈: {np("curedRelative")}',
                f'治愈: {np("crued")}',
                f'新增死亡: {np("diedRelative")}',
                f'死亡: {np("died")}')
        pr('\t'.join(items))
    def sortList(cases):
        return sorted(cases, key=lambda case: int(get_value(case, 'confirmed')), reverse=True)
    for case in sortList(component['caseList']):
        pr(case['area'])
        pr('-' * 20)
        report(case['area'], case)
        for subcase in sortList(case['subList']):
            report('- ' + subcase['city'], subcase)
        pr('-' * 20)

if __name__ == '__main__':
    main()
    os.system('pause')
