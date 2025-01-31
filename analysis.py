{\rtf1\ansi\ansicpg932\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
\
# CSV\uc0\u12501 \u12449 \u12452 \u12523 \u12522 \u12473 \u12488 \u65288 GitHub\u12398 data\u12501 \u12457 \u12523 \u12480 \u12395 \u12354 \u12427 \u12392 \u20206 \u23450 \u65289 \
file_paths = [\
    'data/Data-2024-0924.csv',\
    'data/Data-2024-1001.csv',\
    'data/Data-2024-1008.csv',\
    'data/Data-2024-1015.csv',\
    'data/Data-2024-1022.csv',\
    'data/Data-2024-1029.csv',\
    'data/Data-2024-1105.csv',\
    'data/Data-2024-1112.csv',\
    'data/Data-2024-1126.csv',\
    'data/Data-2024-1203.csv',\
    'data/Data-2024-1210.csv',\
    'data/Data-2024-1217.csv'\
]\
\
# \uc0\u21508 CSV\u12434 \u35501 \u12415 \u36796 \u12435 \u12391 \u32113 \u21512 \
data_frames = [pd.read_csv(file) for file in file_paths]\
combined_data = pd.concat(data_frames, ignore_index=True)\
\
# \uc0\u25237 \u31295 \u25968 \u12392 \u25237 \u31295 \u32773 \u25968 \u12398 \u31639 \u20986 \
file_row_counts = \{file: len(pd.read_csv(file)) for file in file_paths\}\
file_account_counts = \{file: pd.read_csv(file)['account'].nunique() for file in file_paths\}\
\
# \uc0\u12487 \u12540 \u12479 \u12501 \u12524 \u12540 \u12512 \u21270 \
correlation_df = pd.DataFrame(\{\
    "CSV\uc0\u12501 \u12449 \u12452 \u12523 \u12398 \u21517 \u21069 ": list(file_row_counts.keys()),\
    "\uc0\u25237 \u31295 \u25968 ": list(file_row_counts.values()),\
    "\uc0\u25237 \u31295 \u12450 \u12459 \u12454 \u12531 \u12488 \u25968 ": list(file_account_counts.values())\
\})\
\
# \uc0\u24179 \u22343 \u20516 \u12398 \u31639 \u20986 \
mean_post_count = correlation_df["\uc0\u25237 \u31295 \u25968 "].mean()\
mean_account_count = correlation_df["\uc0\u25237 \u31295 \u12450 \u12459 \u12454 \u12531 \u12488 \u25968 "].mean()\
\
print(f"\uc0\u25237 \u31295 \u25968 \u12398 \u24179 \u22343 \u20516 : \{mean_post_count:.2f\}")\
print(f"\uc0\u25237 \u31295 \u32773 \u25968 \u12398 \u24179 \u22343 \u20516 : \{mean_account_count:.2f\}")\
\
# \uc0\u30456 \u38306 \u20418 \u25968 \u12398 \u31639 \u20986 \
correlation = correlation_df["\uc0\u25237 \u31295 \u25968 "].corr(correlation_df["\u25237 \u31295 \u12450 \u12459 \u12454 \u12531 \u12488 \u25968 "])\
print(f"\uc0\u25237 \u31295 \u25968 \u12392 \u25237 \u31295 \u32773 \u25968 \u12398 \u30456 \u38306 \u20418 \u25968 : \{correlation:.3f\}")}