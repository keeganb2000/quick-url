import sys
from qurl import Qurl

launcher = Qurl()


def main():
    try:
        assigned_args = launcher.assign_argument()
        missed_argument = launcher.catch_missing_argument(assigned_args)
        if missed_argument:
            print("You're missing your keyword argument.")
        else:
            valid_argument = launcher.constrain_argument(assigned_args)
            is_valid_argument = launcher.validate_argument(valid_argument)
            if is_valid_argument:
                keyword_list = launcher.check_for_keyword_list(assigned_args)
                if keyword_list:
                    url_csv = launcher.open_url_csv()
                    url_dict = \
                        launcher.convert_url_to_dict(url_csv)
                    printed_keywords = \
                        launcher.print_keywords(url_dict)
                else:
                    url_csv = launcher.open_url_csv()
                    url_dict = \
                        launcher.convert_url_to_dict(url_csv)
                    keyword = \
                        launcher.search_dict(url_dict,
                                             assigned_args)
                    nonetype = launcher.catch_nontype(keyword)
                    if nonetype:
                        print('Keyword argument unknown, try again')
                        sys.exit(0)
                    else:
                        url = \
                            launcher.url_list_to_string(keyword)
                        webbrowser_tab = launcher.open_url(url)
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)


if __name__ == '__main__':
    main()
