import pandas as pd
import re
import sheet_match_enable as smat
import track_modify as tmod
import check_ipo as chki
import check_dl_pf as chkdp


if __name__ == '__main__':
    prefixes = smat.read_leftmost_column_to_list('dat/Prefix.xlsx')
    suffixes = smat.read_leftmost_column_to_list('dat/Suffix.xlsx')
    check_suffixes = smat.read_leftmost_column_to_list('dat/Check Suffix.xlsx')
    check_suffixes = suffixes + prefixes + check_suffixes
    tmod.read_and_clean('dat/Companies.xlsx', 'output/Regex Companies.xlsx',
                        prefixes, suffixes, check_suffixes)
    tmod.read_and_clean('dat/Deallog List.xlsx', 'output/Regex Deallog List.xlsx',
                        prefixes, suffixes, check_suffixes)
    tmod.read_and_clean('dat/Peer Funds.xlsx', 'output/Regex Peer Funds.xlsx',
                        prefixes, suffixes, check_suffixes)
    ipo_df = chki.output_list_ipo('dat/Companies.xlsx',
                         'dat/IPO A.xlsx',
                         'dat/IPO H.xlsx', prefixes,
                         'output/IPO Check.xlsx')
    dl_df, pf_df = chkdp.output_list_dl_pf('dat/Companies.xlsx',
                                           'dat/Deallog List.xlsx',
                                           'dat/Peer Funds.xlsx',
                                           'output/Filtered Deallog List.xlsx',
                                           'output/Filtered Peer Fund List.xlsx',
                                           check_suffixes
                                           )

