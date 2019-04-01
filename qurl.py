import pandas
import os
import webbrowser
import sys
import re
from sys import argv


class Qurl():
    """
    Class defintion: Opens webbrowser when keyword is added as an argument.
    """
    def assign_argument(self):
        """
        Method defintion: define arguments.
        """
        try:
            script, first = argv
            return first
        except Exception:
            pass

    def catch_missing_argument(self, argument):
        if argument is None:
            return True

    def constrain_argument(self, argument):
        """
        Method definition: validates the passed argument for the right length
        and use of permitted characters.
        """
        safe_regex = r"^[A-Za-z0-9._~()'!*:@,;+?-]*$"
        if (len(argument) > 1 and len(argument) < 6
                and re.search(safe_regex, argument)):
            return True
        else:
            return False

    def validate_argument(self, is_argument):
        """
        Method defintion: Checks for True, if present then returned to next
        method. Else stop programme and print error message.
        """
        if is_argument:
            return True
        elif is_argument is False:
            print("Keyword argument is invalid, look at length "
                  "and/or presence of nasty characters.")
            sys.exit(0)
        else:
            print("NoneType passed, problem with application.")

    def check_for_keyword_list(self, argument):
        """
        Method definition: check argument for the string list. This is used in
        part to print out list of key/values that are in the url csv.
        """
        if 'list' in argument:
            return True
        else:
            return False

    def open_url_csv(self):
        """
        Method definition:open qurl url csv into dataframe.
        """
        try:
            open_qurl_url = \
                pandas.read_csv(
                                os.path.join
                                ('~/', 'repos', 'qurl', 'qurl_urls.csv'),
                                header=None
                                )
            return open_qurl_url
        except Exception:
            print("There was an error, "
                  "could not find the file 'qurl_urls.csv'")

    def convert_url_to_dict(self, urls_dataframe):
        """
        Method definition: HoPs url dataframe converted into dictionary.
        """
        try:
            dataframe_to_dict = \
                urls_dataframe.set_index(0).T.to_dict('list')
            return dataframe_to_dict
        except Exception:
            sys.exit(0)

    def print_keywords(self, dict_urls):
        """
        Method defintion: Prints the key/values of url csv file, this is a
        helper so that you can see what your keywords are.
        """
        for key, value in dict_urls.items():
            print('Use the keyword {}, to reach:{}'.format(key, value))

    def search_dict(self, url, argument):
            """
            Method definition:search through url list for chosen key from
            argument.
            """
            for key, value in url.items():
                if argument in key:
                    return value

    def catch_nontype(self, url):
        """
        Method definition: passed datatype from search_dict could be
        NonType, this method is to catch that and end the programme.
        """
        if url is None:
            return True
        else:
            return False

    def url_list_to_string(self, url):
        """
        Method definition: convert url inside list to a string.
        """
        for element in url:
            element.strip('[]')
            return element

    def open_url(self, url):
        """
        Method definition: Launch webbrowser with chosen url.
        """
        try:
            open_tab = webbrowser.open_new_tab(url)
            return open_tab
        except Exception:
            print("There was an error, can't open link in browser")
