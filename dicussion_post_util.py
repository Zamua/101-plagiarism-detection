"""
Utility to receive a list of replies to a discussion post

Documentation here:

https://canvas.beta.instructure.com/doc/api/submissions.html#method.submissions_api.update

"""
import sys
import urllib
import time
import urllib2


class DiscussionPostAccessor(object):

    def __init__(self, key):
        self.url_string = ("https://canvas.jmu.edu/api/v1/"
                           "courses/{}/discussion_topics/{}/entry_list")

        self.url = ""
        self.key = key

    def get_discussion_post_entries(self, course_id, topic_id):
        self.url = self.url_string.format(course_id, topic_id)
        form_data = {}

        data = urllib.urlencode(form_data)
        header = {"Authorization": "Bearer {}".format(self.key)}
        request = urllib2.Request(self.url, data, headers=header)

        for x in range(4):
            try:
                return urllib2.urlopen(request)
            except urllib2.URLError as e:
                print "URL ERROR, trying again " + str(e)
                time.sleep(.5)

        print "Giving up."


if __name__ == "__main__":
    # CS 101 ID
    COURSE_ID = "1517997"

    # Post 07: Algorithms for illegal - Mayfield 1
    TOPIC_ID = "5729010"

    gp = DiscussionPostAccessor(sys.argv[1])
    response = gp.get_discussion_post_entries(COURSE_ID, TOPIC_ID)

    if response is not None:
        print response.read()
