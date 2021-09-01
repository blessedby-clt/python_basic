from bs4 import BeautifulSoup

# read xml file
with open("ipa110106.XML", "r", encoding="utf8") as xml_file:
    xml = xml_file.read()

print(xml)

xml_list = xml.split('<?xml version="1.0" encoding="UTF-8"?>')

## ''을 제외시키기
if '' in xml_list :
    xml_list.remove('')

# csv 파일 만들기 전 세팅.
header = ["등록번호", "등록일자", "출원번호", "출원일자", "상태", "특허제목"]
data_list = []
data_list.append(header)
print(data_list)

for page in xml_list :
    soup = BeautifulSoup(page, "lxml")
    publication_reference_tag = soup.find("publication-reference")
    application_reference_tag = soup.find("application-reference")
    p_document_id_tag = publication_reference_tag.find("document-id")
    a_document_id_tag = application_reference_tag.find("document-id")

    p_doc_number = p_document_id_tag.find("doc-number").get_text()  # 등록번호
    p_date = p_document_id_tag.find("date").get_text()              # 등록일자
    a_doc_number = a_document_id_tag.find("doc-number").get_text()  # 출원번호
    a_date = a_document_id_tag.find("date").get_text()              # 출원일자
    p_kind = p_document_id_tag.find("kind").get_text()              # 상태
    invention_title = soup.find("invention-title").get_text()       # 특허제목

    # make data_list
    data_list.append([p_doc_number, p_date, a_doc_number, a_date, p_kind, invention_title])
    print(data_list)
with open ("pub_info.csv", "w") as pub_info:
    for d in data_list:
        pub_info.write(",".join(d).strip('\n')+"\n")
