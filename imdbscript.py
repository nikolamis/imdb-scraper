from lxml import html
import requests

import csv




with open('mycsv.csv','w') as f:

    #drugi
    def funk2(string,X):
        broj = 1
        strana = requests.get(string)
        tree = html.fromstring(strana.content)
        filmovi = tree.xpath('//tbody[@class="lister-list"]//td[@class="titleColumn"]//a/text()')
        ocene = tree.xpath('//tbody[@class="lister-list"]//td[@class="ratingColumn imdbRating"]//strong/text()')

        for film in filmovi:
            #print (broj , film, ocene[broj])
            fieldnames =[broj,film,ocene[broj]]
            thewriter = csv.DictWriter(f,fieldnames=fieldnames)

            thewriter.writeheader()
            broj=broj+1
            if X < broj:
                break


    #best motion picture
    def funk3a(string,year):
        broj=0
        strana = requests.get(string)
        tree = html.fromstring(strana.content)
        filmovi = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-advanced"]//div[@class="lister-item-content"]//h3[@class="lister-item-header"]//a/text()')
        godina = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-advanced"]//div[@class="lister-item-content"]//h3[@class="lister-item-header"]//span[@class="lister-item-year text-muted unbold"]/text()')

        for film in filmovi:
            temp='('
            temp2=str(year)
            temp3=')'
            tt=temp+temp2+temp3
            at='(I) '+tt #covering the few examples because imdb wrote like that

            if (godina[broj]==tt) or (godina[broj]==at):
                #print (film, godina[broj])
                naziv="best motion picture-->"
                fieldnames =[naziv,film,godina[broj]]
                thewriter = csv.DictWriter(f,fieldnames=fieldnames)

                thewriter.writeheader()
                break
            broj=broj+1
            #91 is max, because 1st film to recive award was 1927
            if broj>91:
                break
            #1 problem can occur, there are movie that was released in the end of 2008
            #and won award for best movie of 2009.
            #i could solve this by 1st counting how many movies went out that year and if it was more than 2
            #pick 1st if year was matching if year was != i would pick 2nd movie

    #visual effects
    def funk3e(string,year):
        broj=0 #when i put 1 it always go 1 movie before
        strana = requests.get(string)
        tree = html.fromstring(strana.content)
        filmovi = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-detail"]//div[@class="lister-item-content"]//h3[@class="lister-item-header"]//a/text()')
        godina = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-detail"]//div[@class="lister-item-content"]//h3[@class="lister-item-header"]//span[@class="lister-item-year text-muted unbold"]/text()')
        for film in filmovi:
            temp='('
            temp2=str(year)
            temp3=')'
            tt=temp+temp2+temp3

            if godina[broj]==tt:

                #print (film, godina[broj])
                naziv="best visual effect-->"
                fieldnames =[naziv,film,godina[broj]]
                thewriter = csv.DictWriter(f,fieldnames=fieldnames)

                thewriter.writeheader()
                break
            broj=broj+1
            if broj>78:
                break
    #screenplay
    def funk3d(string,year):
        broj=0
        strana = requests.get(string)
        tree = html.fromstring(strana.content)
        filmovi = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-detail"]//div[@class="lister-item-content"]//h3[@class="lister-item-header"]//a/text()')
        godina = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-detail"]//div[@class="lister-item-content"]//h3[@class="lister-item-header"]//span[@class="lister-item-year text-muted unbold"]/text()')
        for film in filmovi:
            temp='('
            temp2=str(year)
            temp3=')'
            tt=temp+temp2+temp3
            at='(I) '+tt #covering the few examples because imdb wrote like that

            if (godina[broj]==tt) or (godina[broj]==at):
                #print (film, godina[broj])
                naziv="best screenplay-->"
                fieldnames =[naziv,film,godina[broj]]
                thewriter = csv.DictWriter(f,fieldnames=fieldnames)

                thewriter.writeheader()
                break
            broj=broj+1
            if broj>36:
                break

    #actor and actress
    def funk3bc(string,year):
        broj=0
        strana = requests.get(string)
        tree = html.fromstring(strana.content)
        glumci = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-detail"]//div[@class="lister-item-content"]//h3[@class="lister-item-header"]//a/text()')#ime
        godina = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-detail"]//div[@class="list-description"]//p//b/text()')#opis

        for glumac in glumci:
            temp=str(year)
            if temp in godina[broj]:
                #print(glumac) # i can add ,godina and there would be name of charachter and name of movie
                naziv="best male and female acctor-->"
                fieldnames =[naziv,glumac]
                thewriter = csv.DictWriter(f,fieldnames=fieldnames)

                thewriter.writeheader()
                break
            broj=broj+1
            if broj>89:
                break

    #genre
    def funk2d(string):
        broj = 1
        strana = requests.get(string)
        tree = html.fromstring(strana.content)
        filmovi = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-advanced"]//div[@class="lister-item-content"]//h3[@class="lister-item-header"]//a/text()')
        ocene = tree.xpath('//div[@class="lister-list"]//div[@class="lister-item mode-advanced"]//div[@class="lister-item-content"]//div[@class="ratings-bar"]//div[@class="inline-block ratings-imdb-rating"]//strong/text()')
        for film in filmovi:
            #print (broj , film,ocene[broj])

            fieldnames =[broj,film,ocene[broj]]
            thewriter = csv.DictWriter(f,fieldnames=fieldnames)

            thewriter.writeheader()
            broj=broj+1
            if X < broj:
                break



    #output za prvi
    X=int(input("number of movies?"))
    answ= input("choose filter: a)IMDb rating b)Ranking c)Release Date d)Genre\n").lower()

    if answ == 'a':
        funk2('https://www.imdb.com/chart/top?sort=ir,desc&mode=simple&page=1',X)

    elif answ =='b':
        funk2('https://www.imdb.com/chart/top?sort=rk,asc&mode=simple&page=1',X)

    elif answ =='c':
        funk2('https://www.imdb.com/chart/top?sort=us,desc&mode=simple&page=1',X)


    elif answ =='d':
        genre=input("write down genre you want(comedy/adventure/horror etc) ").lower()
        link1="https://www.imdb.com/search/title?genres="
        link2="&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=HTM54141ZA1J3FDZMGMQ&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_7"
        link=link1+genre+link2
        funk2d(link)


    #output za drugi
    year= int(input("enter year: "))
    print("Wait a moment")
    print(".")
    funk3a("https://www.imdb.com/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc",year)
    print(".")
    funk3d("https://www.imdb.com/list/ls025251338",year)
    print(".")
    funk3e("https://www.imdb.com/list/ls000513539/",year)
    print(".")
    funk3bc("https://www.imdb.com/list/ls055244920/",year)
    print(".")
    funk3bc("https://www.imdb.com/list/ls055244524/",year)

    print("u have ur output in csv file -->")
