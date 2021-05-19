def get_cands(kw1="data scientist", kw2="istanbul",kw3 = "", kw4="", kw5="", kw6 ="",kw7 ="", page_n=1):
    from .pmeters1 import password1, mail1
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from time import sleep
    import pandas as pd

    newdf = pd.DataFrame(columns=["Name",
                                  "User Profile",
                                  "Email",
                                  "Website",
                                  "Location",
                                  "Status",
                                  "Title",
                                  "Experience 1",
                                  "Experience 2",
                                  "Experience 3",
                                  "Ex-Company 1",
                                  "Ex-Company 2",
                                  "Ex-Company 3",
                                  "Education 1",
                                  "Education 2",
                                  "Education 3",
                                  "Skill 1",
                                  "Skill 2",
                                  "Skill 3",
                                  "Language 1",
                                  "Language 2",
                                  "Language 3",
                                  "Certification 1",
                                  "Certification 2",
                                  "Certification 3"])

    driver = webdriver.Chrome()
    driver.get('https://www.linkedin.com')
    username = driver.find_element_by_class_name('input__input')
    username.send_keys(mail1)
    password = driver.find_element_by_name('session_password')
    password.send_keys(password1)

    log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
    log_in_button.click()

    #google

    the_query = 'site:linkedin.com/in/ AND "'+ kw1+ '" AND "'+ kw2 +'" AND "'+kw3+'" AND "'+ kw4 +'" AND "'+kw5 + '" AND "'+kw6+'" AND "'+kw7+'"'
    driver.get("https://www.google.com/")
    search_query = driver.find_element_by_name('q')
    search_query.send_keys(the_query)
    search_query.send_keys(Keys.RETURN)


    linkedin_urls = []
    ppp = 1
    while ppp<=page_n:
        print("Getting Links From Page ",ppp)
        links = driver.find_elements_by_tag_name("a")
        linkedin_urls1 = [url.get_attribute("href") for url in links]

        for linkedin_url in linkedin_urls1:
            try:
                if "google" not in linkedin_url and "linkedin" in linkedin_url:
                    linkedin_urls.append(linkedin_url)
            except:
                pass

        driver.find_element_by_xpath("//*[contains(local-name(), 'span') and contains(text(), 'Sonraki')]").click()
        ppp = ppp +1


    for i in linkedin_urls:
        print(i)


    for url1 in linkedin_urls:


        driver.get(url1)
        sleep(1)

        name = driver.find_elements_by_xpath('//li[@class="inline t-24 t-black t-normal break-words"]')
        name1 = name[0].text
        print("")
        print("name: ", name1)
        sleep(0.2)
        print("User Profile: ", url1)

        the_c = driver.find_element_by_xpath('//span[@class="t-16 link-without-visited-state"]')
        the_c.click()
        sleep(1)
        t_web=""

        try:
            t1234 = driver.find_element_by_xpath('//a[@class="pv-contact-info__contact-link link-without-visited-state"]')
            t_web=t1234.text
        except:
            pass

        print("Website: ", t_web)

        e_mail = ""

        try:
            e1234 = driver.find_element_by_xpath('//section[@class="pv-contact-info__contact-type ci-email"]')
            e_mail = e1234.text.split("\n")[1]
        except:
            pass

        print("Email: ",e_mail)

        sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()




        gg=0
        while gg<30 :
            driver.execute_script("window.scrollBy(0,200);")
            sleep(0.1)
            gg += 1

        sleep(1)
        location = driver.find_element_by_xpath('//li[@class="t-16 t-black t-normal inline-block"]')
        location1 = location.text
        print("location: ", location1)
        sleep(0.2)

        cur_title = driver.find_elements_by_xpath('//h2[@class="mt1 t-18 t-black t-normal break-words"]')
        the_title = cur_title[0].text
        print("current title: ", the_title)
        sleep(1)



        experience = driver.find_elements_by_css_selector('#experience-section .pv-profile-section')
        ex_comps= []
        work_hist = []
        for r in experience:

            if r.text[:6]=="Şirket":

                exxc = r.text.split("Toplam Süre")[0].split("Adı")[1]


                lisd1 = r.text.split("Unvan")
                for x in lisd1[1:]:
                    lisd2= x.split("Çalışma Tarihleri")
                    work_hist.append(lisd2[0])
                    ex_comps.append(exxc)
            else:
                lisd1 = r.text.split("Şirket")
                work_hist.append(lisd1[0])
                exxc = r.text.split("Çalışma Tarihleri")[0].split("Adı")[1]

                if "Tam zamanlı" in exxc:
                    exxc = exxc.split("Tam zamanlı")[0]

                ex_comps.append(exxc)


        print("experience:",work_hist)
        print("ex-companies:", ex_comps)

        if len(work_hist)<3:
            for i in range(3-len(work_hist)):
                work_hist.append("")


        if len(ex_comps)<3:
            for i in range(3-len(ex_comps)):
                ex_comps.append("")


        exp1, exp2, exp3 = work_hist[:3]
        exp1, exp2, exp3 = exp1.strip(), exp2.strip(), exp3.strip()
        exc1, exc2, exc3 = ex_comps[:3]
        exc1, exc2, exc3 =  exc1.strip(), exc2.strip(), exc3.strip()

        sleep(0.2)

        the_s = False
        the_stat=""
        for ex in experience:
            if "Şu Anda" in ex.text:
                the_s = True

        if the_s:
            the_stat = "Employed"
        else:
            the_stat = "Unemployed"

        print("Status: ",the_stat)
        sleep(.2)






        university = driver.find_elements_by_xpath('//h3[@class="pv-entity__school-name t-16 t-black t-bold"]')
        sch_hist = []

        try:
            for u in university:
                sch_hist.append(u.text)
        except:
            pass

        print("education: ", sch_hist)

        if len(sch_hist) < 3:
            for i in range(3 - len(sch_hist)):
                sch_hist.append("")

        sch1, sch2, sch3 = sch_hist[:3]
        sch1, sch2, sch3 = sch1.strip(), sch2.strip(), sch3.strip()

        sleep(0.2)

        skills = driver.find_elements_by_xpath('//span[@class="pv-skill-category-entity__name-text t-16 t-black t-bold"]')
        the_skill = []

        try:
            for s in skills:
                the_skill.append(s.text)
        except:
            pass

        print("skills: ", the_skill)

        if len(the_skill) < 3:
            for i in range(3 - len(the_skill)):
                the_skill.append("")

        skl1, skl2, skl3 = the_skill[:3]
        skl1, skl2, skl3 = skl1.strip(), skl2.strip(), skl3.strip()
        sleep(0.2)

        try:
            try:
                langs = driver.find_element_by_xpath(
                    '//section[@class="pv-profile-section pv-accomplishments-block languages pv-accomplishments-block--last ember-view"]')
            except:
                langs = driver.find_element_by_xpath(
                    '//section[@class="pv-profile-section pv-accomplishments-block languages ember-view"]')

            langs = langs.text

            the_ind = 0
            for n, i in enumerate(langs.split()):
                if i == "Dil":
                    the_ind = n
                else:
                    pass

            the_langs = langs.split()[the_ind + 1:]

        except:
            the_langs=[]

        print("languages: ", the_langs)

        if len(the_langs) < 3:
            for i in range(3 - len(the_langs)):
                the_langs.append("")

        lng1, lng2, lng3 = the_langs[:3]
        lng1, lng2, lng3 = lng1.strip(), lng2.strip(), lng3.strip()
        sleep(0.2)

        licences = driver.find_elements_by_xpath('//h3[@class="t-16 t-bold"]')
        the_licences = []
        try:
            for lc in licences:
                the_licences.append(lc.text)

        except:
            pass


        print("certifications: ", the_licences)
        print("")

        if len(the_licences) < 3:
            for i in range(3 - len(the_licences)):
                the_licences.append("")

        lcn1, lcn2, lcn3 = the_licences[:3]
        lcn1, lcn2, lcn3 = lcn1.strip(), lcn2.strip(), lcn3.strip()
        dict1 = {"Name":name1,
                 "User Profile":url1,
                 "Email": e_mail,
                 "Website": t_web,
                 "Location":location1,
                 "Status":the_stat,
                 "Title":the_title,
                 "Experience 1": exp1,
                 "Experience 2": exp2,
                 "Experience 3": exp3,
                 "Ex-Company 1": exc1,
                 "Ex-Company 2": exc2,
                 "Ex-Company 3": exc3,
                 "Education 1": sch1,
                 "Education 2": sch2,
                 "Education 3": sch3,
                 "Skill 1": skl1,
                 "Skill 2": skl2,
                 "Skill 3": skl3,
                 "Language 1": lng1,
                 "Language 2": lng2,
                 "Language 3": lng3,
                 "Certification 1": lcn1,
                 "Certification 2": lcn2,
                 "Certification 3": lcn3}

        newdf = newdf.append(dict1, ignore_index=True)



    driver.quit()
    thepath = kw1+"_"+kw2+".csv"
    newdf.to_csv(thepath, index=False, encoding="utf-8-sig")
    return newdf







