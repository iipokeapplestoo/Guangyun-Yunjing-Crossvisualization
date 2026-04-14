# Maps each distinct rime class (韻) WITHIN the Rime Table Position (音韻地位) field of 廣韻.csv to one of the 16 rime group (shè 攝) groupings used to organize rime tables.

# CAUTION: In dataframe Guangyun_final, there are two columns dealing with rime names:
# 1) Guangyun rime (韻目原貌): extracted directly from 廣韻.csv; gives the name of the rime based on the GUANGYUN system.
# 2) rime class: extracted from RTP field within 廣韻.csv; gives the name of the rime class based on the QIEYUN system.
# Differences between Qieyun and Guangyun rime classes (RC):
#   - 殷 character is used instead of 欣 for 殷RC. Cosmetic change.
#   - 諄RC is merged into 真RC. 
#   - 桓RC is merged into 寒RC.
#   - 戈RC is merged into 歌RC.
# Tone (平上去入) is encoded separately in the tone field, so each RC here covers all four tonal variants (e.g. 東RC = 東/董/送/屋 rimes).

# Sources: 
# 1) List of 206 Guangyun rimes: Dong Tonghe, Historical Phonology of Chinese, trans. Wang Pin (Routledge, 2024), 84-85.
# 2) nk2028 Qieyun rime table position and rime class data: https://nk2028.shn.hk/tshet-uinh-js/classes/____-1.html

rimeClass_to_rimeGroup = {
    # 通攝 (tōng) — Tables 1–2 in Yunjing
    '東': '通',
    '冬': '通',
    '鍾': '通',

    # 江攝 (jiāng) — Table 3
    '江': '江',

    # 止攝 (zhǐ) — Tables 4–8
    '支': '止',
    '脂': '止',
    '之': '止',
    '微': '止',

    # 遇攝 (yù) — Tables 9–10
    '魚': '遇',
    '虞': '遇',
    '模': '遇',

    # 蟹攝 (xiè) — Tables 11–16
    '齊': '蟹',
    '祭': '蟹',
    '泰': '蟹',
    '佳': '蟹',
    '皆': '蟹',
    '夬': '蟹',
    '灰': '蟹',
    '咍': '蟹',
    '廢': '蟹',

    # 臻攝 (zhēn) — Tables 17–20
    '真': '臻',
    '臻': '臻',
    '文': '臻',
    '殷': '臻',
    '魂': '臻',
    '痕': '臻',

    # 山攝 (shān) — Tables 21–26
    '元': '山',
    '寒': '山',
    '刪': '山',
    '山': '山',
    '先': '山',
    '仙': '山',

    # 效攝 (xiào)
    '蕭': '效',
    '宵': '效',
    '肴': '效',
    '豪': '效',

    # 果攝 (guǒ)
    '歌': '果',

    # 假攝 (jiǎ)
    '麻': '假',

    # 宕攝 (dàng) — Tables 31–32
    '陽': '宕',
    '唐': '宕',

    # 梗攝 (gěng) — Tables 33–36
    '庚': '梗',
    '耕': '梗',
    '清': '梗',
    '青': '梗',

    # 曾攝 (céng) — Tables 42–43
    '蒸': '曾',
    '登': '曾',

    # 流攝 (liú)
    '尤': '流',
    '侯': '流',
    '幽': '流',

    # 深攝 (shēn)
    '侵': '深',

    # 咸攝 (xián) — Tables 39–41
    '覃': '咸',
    '談': '咸',
    '鹽': '咸',
    '添': '咸',
    '咸': '咸',
    '銜': '咸',
    '嚴': '咸',
    '凡': '咸',
}

# Canonical ordering of the 16 攝, following the traditional sequence.
# Used to order the heatmap y-axis.
rimeGroup_order = [
    '通', '江', '止', '遇', '蟹', '臻', '山', '效',
    '果', '假', '宕', '梗', '曾', '流', '深', '咸',
]
