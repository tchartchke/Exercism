
import re

def parse(markdown):

    #mark bold and italics
    marked_list = re.findall(r'__+|[^__]+|_', markdown)
    curr_i = False
    curr_b = False
    for n in range(len(marked_list)):
        if marked_list[n] == '__':
            if not curr_b:
                marked_list[n] = '<strong>'
            else:
                marked_list[n] = '</strong>'
            curr_b = not curr_b
        elif marked_list[n] == '_':
            if not curr_i:
                marked_list[n] = '<em>'
            else:
                marked_list[n] = '</em>'
            curr_i = not curr_i

    markdown = ''.join(marked_list)
    marked_list = markdown.split('\n')

    list_start = True
    for n in range(len(marked_list)):
        #set and change headers

        if marked_list[n][0] == '#':
            headcount = 0
            while marked_list[n][headcount] == '#': headcount += 1
            marked_list[n] = '<h{}>{}</h{}>'.format(headcount, marked_list[n][headcount+1:], headcount)

        #mark lists
        elif marked_list[n][0] == '*':
            marked_list[n] = '<li>'+marked_list[n][2:]+'</li>'
            if list_start:
                marked_list[n] = '<ul>'+marked_list[n]
                list_start = False
            
            #Close list
            if n+1 >= len(marked_list):
                marked_list[n] = marked_list[n]+'</ul>'
                list_start = True
            else:
                if marked_list[n+1][0] != '*':
                    marked_list[n] = marked_list[n]+'</ul>'
                    list_start = True
   
        #mark paragraphs
        else:
            marked_list[n] = '<p>'+marked_list[n]+'</p>'

    return ''.join(marked_list)