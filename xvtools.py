import streamlit as st
from pytube import YouTube
import pandas as pd
import requests
import pyperclip
from bs4 import BeautifulSoup 

st.set_page_config(
    page_title="XvTools",
    )



with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.text("----- XvTools -----")
        st.text("------ By --------")
        st.text("---- Cyper24 -----")
        
    with col2:
        option = st.selectbox(
        'Select Tool',
        ('YouTube Keyword', 'T0KP3D $CRAPPER', 'ExTracTor'))

    st.text(" ")
    st.text("$=================================================================================$")
    st.text(" ")
    col5, col6,col7 = st.columns(3)

# yt keyword


if option =="YouTube Keyword":
    
    with col6:
        st.text('$/$ YouTube Keyword $/$')
    cari = st.text_input('URL')
    st.text("---- Result ----")
    try:
        yt = YouTube(cari)
        n = yt.title
        a = yt.author
        x = yt.keywords 
        r = yt.rating    
        st.text("Title = " + n +" - "+ a)
        col3, col4 = st.columns(2)
        with col3: 
            cp = st.text_area("Keyword",','.join(x))
        with col4:
            st.text("--")
            if st.button('Copy'):
                pyperclip.copy(cp)
    except:
        st.caption(" ")
    
    st.text('$/$ Made with ❤ By Cyper24 $/$')


# Tokped

elif option =="T0KP3D $CRAPPER":
    with col6:
        st.text('$/$ T0KP3D $CRAPPER $/$')
    st.text('Non TopAds | Max 995 result | Kalo lama ditunggu aja')                                
    cari = st.text_input('Cari Apa? ')
    products = []
    try:
        for i in range(0, 1000, 200):
                query = """query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      banner {\n        position\n        text\n        imageUrl\n        url\n        componentId\n        trackingOption\n        __typename\n      }\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"""
                variables = {"params": "device=desktop&navsource=&ob=23&q={0}&related=true&rf=true&rows=200&safe_search=false&scheme=https&shipping=&shop_tier=&source=search&srp_component_id=01.07.00.00&srp_page_id=&srp_page_title=&st=product&start={1}&topads_bucket=true&unique_id=50b1941cafe02034467cf2021ef2e068&user_addressId=&user_cityId=&user_districtId=2274&user_id=&user_lat=&user_long=&user_postCode=&user_warehouseId=&variants=".format(cari,i)}
                response = requests.post('https://gql.tokopedia.com/graphql/SearchProductQueryV4/',json={"query": query, "variables": variables})
                r = response.json()
                for x in range(1,200):
                        name = r['data']['ace_search_product_v4']['data']['products'][x]['name']
                        url = r['data']['ace_search_product_v4']['data']['products'][x]['url']
                        price = r['data']['ace_search_product_v4']['data']['products'][x]['price']
                        shop = r['data']['ace_search_product_v4']['data']['products'][x]['shop']['name']
                        city = r['data']['ace_search_product_v4']['data']['products'][x]['shop']['city']
                        review = r['data']['ace_search_product_v4']['data']['products'][x]['countReview']
                        try:
                                title = r['data']['ace_search_product_v4']['data']['products'][x]['badges'][0]['title']
                        except:
                                title = ("None")
                        data = {'Name' : name,'Price':price,'Shop' : shop,'City' : city,'Badge' : title,'Review Count':review,'Link': url }
                        products.append(data)
        df = pd.DataFrame(products)
        df.index += 1
        st.dataframe(df,1000, 1000)
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='List.csv',
            mime='text/csv',)

    except:
        st.text(' ')

    st.text('$/$ Made with ❤ By Cyper24 $/$')

elif option =="ExTracTor":
    list1 = []
    list2 = []
    col1, col2, col3 = st.columns(3)
    with col2:
        st.text("$/$ AnimeExTracTor $/$")

    cari_an = st.text_input('What Do You want?', '')
    try:
        main_url = "https://samehadaku.win/?s={}".format(cari_an)
        res_search = requests.get(main_url)
        soup_search = BeautifulSoup(res_search.content,'lxml')
        list_search = soup_search.find_all("div", class_='animepost')
        for result in list_search:
            name_search = result.find("div", class_='title').text
            link_search = result.find("a").attrs['href']
            data_search = {"Anime Name" : name_search, "link" :link_search}
            list1.append(data_search)
        dfsearch = pd.DataFrame(list1)
        st.table(dfsearch['Anime Name'])

        cari = int(st.text_input('Select Anime', ''))
        dfanime = dfsearch.iloc[cari]
        link_anime = dfanime[1]

        res_anime = requests.get(link_anime)
        soup_anime = BeautifulSoup(res_anime.content,'lxml')
        animen = soup_anime.find_all("div", class_='epsleft')
        for x2 in animen:
            name_anime = x2.find("a").text
            link_anime = x2.find("a").attrs["href"]
            data_anime = {"Anime Name" : name_anime, "link" :link_anime}
            list2.append(data_anime)
        dfdownanime = pd.DataFrame(list2)
        st.table(dfdownanime['Anime Name'])

        cari2 = int(st.text_input('Select Episode', ''))
        dffinal = dfdownanime.iloc[cari2]
        linkfinal = dffinal[1]

        res_final = requests.get(linkfinal)
        soup_final = BeautifulSoup(res_final.content,'lxml')
        titlee = soup_final.find("title").text
        st.markdown(":green[**********]" + titlee + ":green[**********]")
        anime_final = soup_final.find_all("div", class_='download-eps')
        for f in anime_final:
            name_final = f.find("ul")
            col = f.find("p").text
            st.markdown(":red[------------------------------------]" + col + ":red[------------------------------------]")
            for xx in name_final:
                s = xx.find("strong").text
                st.markdown(":blue[-------------]" + s)
                name2final = xx.find_all("span")
                for xxx in name2final:
                    llfinal = xxx.find("a").attrs["href"]
                    st.markdown(":green[+]" + llfinal)

    except:
        st.text(" ")
    st.text('$/$ Made with ❤ By Cyper24 $/$')
