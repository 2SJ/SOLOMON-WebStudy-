from django.http import HttpResponse
from board.models import DjangoBoard
from django.shortcuts import render_to_response

rowsPerPage = 5
def boardView(request):

    boardList = DjangoBoard.objects.order_by('-id')[0:5]
    current_page = 1
    totalCnt = DjangoBoard.objects.all().count()

    pagingHelperIns = pagingHelper()
    totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)
    print ('totalPageList', totalPageList)

    return render_to_response('listSpecificPage.html', {'boardList':boardList,
    'totalCnt':totalCnt, 'current_page':current_page, 'totalPageList': totalPageList})

class pagingHelper:

    def getTotalPageList(self, total_cnt, rowsPerPage):
        if ((total_cnt % rowsPerPage) == 0):
            self.total_pages = int(total_cnt / rowsPerPage)
            print ('getTotalPage #1')
        else:
            self.total_pages = int(total_cnt / rowsPerPage) + 1
            print ('getTotalPage #2')

        self.totalPageList = []
        for j in range(self.total_pages):
            self.totalPageList.append(j + 1)

        return self.totalPageList

    def __init__(self):
        self.total_pages = 0
        self.totalPageList = 0