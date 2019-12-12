import glob
import os

from datetime import datetime


def get_current_time():
    # print(datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
    return(datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))


def read_template(file_path):
    pass

def gen_html_by_slide_images(dir_path):

    os.chdir(dir_path)
    files = glob.glob("./*")

    count = len(files)

    txt = []
    
    for i in range(count):
        t = (
            "<!-- page : {} -->\n"
            "<div class=\"slide\">\n"
            "<div class=\"image\">\n"
            "<img src=\"../slide_images/slide_{}.png\" width=\"100%\" height=\"auto\"></img>\n"
            "<p>{} / {}</p>\n"
            "</div>\n"
            "<!-- // insert -->\n"
            "\n"
            "<!-- insert // -->\n"
            "</div>\n"
            "<br><hr><br>\n\n").format(i+1, i+1, i+1, count)

        # print(t)
        txt.append(t)
        # print(txt)
    return txt


def write_file(fp, write_objs):
    f = open(fp, "w")
    f.writelines(write_objs)






def build_html(dir_path, insert_txt):

    f = open(dir_path+"/master.html", "r")
    fr = f.readlines()
    f.close()

    joined ="".join(insert_txt)
    # print(joined)

    out = []
    for i in range(len(fr)):
        line = fr[i]
        line = line.replace("$ALL_LINK", joined)
        out.append(line)
    now = get_current_time()

    ### override mode
    write_file(dir_path+"/index.html", out)

    ### new file
    # write_file(dir_path+"/index_" + str(now) + ".html", out)

    print("build complete!")



_insert_ = gen_html_by_slide_images("../slide_images")
build_html("../PRESENTATION", _insert_)