

======== FILE: build_amrest.py ========

from pathlib import Path
# Reuse only the existing fonts and layout setup, without rebuilding the older CV.
exec((Path(__file__).parent/'build_draco.py').read_text(encoding='utf-8-sig').split('blocks=[')[0])
styles['section'].spaceBefore=8
styles['body'].leading=12
styles['bullet'].leading=12
blocks=[
('name','Denis Gruszkiewicz'),
('role','IT Menu Junior Administrator | wsparcie aplikacji i testowanie zmian'),
('contact','Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com'),
('contact','Portfolio projektowe: github.com/Flyingzaptop'),
('section','PROFIL ZAWODOWY'),
('body','Młodszy Administrator IT z ponad rokiem doświadczenia we wsparciu użytkowników i rozwiązywaniu problemów aplikacyjnych w szpitalu. Testuję scenariusze działania, odtwarzam błędy i rozwijam narzędzia usprawniające codzienną pracę. Bardzo dobrze znam Microsoft 365, pracuję z Windows i podstawami Linuxa oraz mam podstawy SQL i praktykę projektową z bazami danych. Chcę wykorzystać to zaplecze w IT Menu Management w AmRest: przy testowaniu zmian, wsparciu systemów i automatyzacji procesów.'),
('section','KLUCZOWE KOMPETENCJE'),
('bullet','Wsparcie aplikacji i użytkowników: rozpoznawanie problemów, diagnoza, odtwarzanie błędów i wyjaśnianie sposobu działania systemów.'),
('bullet','Testowanie zmian: sprawdzanie scenariuszy, walidacja danych, kontrola reguł procesu i weryfikacja poprawek.'),
('bullet','Microsoft 365 / MS Office - bardzo dobra znajomość; Windows i podstawy Linuxa.'),
('bullet','Podstawy SQL; projektowa praca z PostgreSQL i SQLite, strukturą danych oraz logiką aplikacji.'),
('bullet','Automatyzacja i aplikacje webowe: Python, Django, React/TypeScript, n8n; dokumentacja techniczna i analiza potrzeb użytkowników.'),
('section','DOŚWIADCZENIE ZAWODOWE'),
('title','Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie'),
('bullet','Bieżące wsparcie pracowników w obsłudze systemów oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych.'),
('bullet','Testowanie scenariuszy działania i logiki aplikacji, odtwarzanie zgłaszanych błędów oraz sprawdzanie poprawności danych.'),
('bullet','Analiza potrzeb użytkowników i rozwój wewnętrznych narzędzi upraszczających powtarzalne czynności.'),
('bullet','Praca nad oddzielnymi rozwiązaniami do zarządzania pracownikami, grafikiem oraz procesami laboratoryjnymi.'),
('bullet','Konfiguracja stanowisk i urządzeń sieciowych, podstawowa diagnostyka połączeń oraz dołączanie komputerów do domeny.'),
('section','WYBRANE PROJEKTY'),
('title','LabFlow | aplikacja procesowa Django / React'),
('body','Demonstracyjny system koordynacji pracy laboratorium: etapy, statusy, formularze, role użytkowników i historia operacji. PostgreSQL/SQLite, testy reguł aplikacji oraz dokumentacja użytkownika i techniczna. Praktyka przekładania procesu użytkownika na czytelne zasady działania systemu.'),
('title','JobHunter | automatyzacja workflow'),
('body','n8n, Node.js, PostgreSQL i Playwright; porządkowanie danych, walidacja schematów, panel React oraz testy i GitHub Actions CI. Projekt rozwijany lokalnie.'),
('section','WYKSZTAŁCENIE'),
('title','WSB Merito we Wrocławiu | 03.2026 - obecnie'),
('body','Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr.'),
('title','Politechnika Wrocławska | 10.2022 - obecnie'),
('body','Robotyka i Automatyzacja Procesów, studia inżynierskie; ukończony V semestr.'),
('section','JĘZYKI I INFORMACJE DODATKOWE'),
('body','Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. IT Step: kurs Python AI, 02.2024 - 12.2024.'),
('body','Dodatkowa praktyka: analiza danych w Pythonie oraz projekty Fusion 360, AutoCAD i RobotStudio. Prawo jazdy kat. B. Zainteresowanie pełnym etatem w modelu hybrydowym; termin rozpoczęcia do uzgodnienia.'),
]
def footer(c,d):
 c.setStrokeColor(HexColor('#D9E2E9'));c.line(42,36,A4[0]-42,36);c.setFont('CV',7);c.setFillColor(HexColor('#556475'));c.drawString(42,24,'Denis Gruszkiewicz | r3dflzp.ns@gmail.com')
story=[]
for kind,t in blocks:
 p=Paragraph(escape(('- ' if kind=='bullet' else '')+t),styles[kind]);p.keepWithNext=kind in ['title','section'];story.append(p)
path=out/'Denis_Gruszkiewicz_CV_AmRest_IT_Menu_PL.pdf'
SimpleDocTemplate(str(path),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=32,bottomMargin=46,title='Denis Gruszkiewicz - AmRest IT Menu Junior Administrator',author='Denis Gruszkiewicz').build(story,onFirstPage=footer,onLaterPages=footer)
(out/'AmRest_content.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
import pdfplumber,pypdfium2 as pdfium
with pdfplumber.open(path) as pdf:
 t=' '.join(p.extract_text() or '' for p in pdf.pages)
 assert len(pdf.pages)==1,len(pdf.pages)
 assert all(s in t for s in ['r3dflzp.ns@gmail.com','AmRest','SQL','II semestr','V semestr'])
 print('1 page; contact/education/content checks OK')
doc=pdfium.PdfDocument(str(path));doc[0].render(scale=1.4).to_pil().save(root/'tmp/pdfs/amrest-1.png')




======== FILE: build_cyclo_portfolio.py ========

from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader,PdfWriter
root=Path('C:/Users/r3d_flzp/Desktop/manualCV')
pdfmetrics.registerFont(TTFont('CV','C:/Windows/Fonts/arial.ttf'));pdfmetrics.registerFont(TTFont('CVB','C:/Windows/Fonts/arialbd.ttf'))
styles={
 'name':ParagraphStyle('name',fontName='CVB',fontSize=23,leading=28,textColor=HexColor('#172535'),spaceAfter=8),
 'title':ParagraphStyle('title',fontName='CVB',fontSize=14,leading=19,textColor=HexColor('#17617A'),spaceAfter=10),
 'head':ParagraphStyle('head',fontName='CVB',fontSize=10,leading=14,textColor=HexColor('#17617A'),spaceBefore=12,spaceAfter=5),
 'body':ParagraphStyle('body',fontName='CV',fontSize=10,leading=14,textColor=HexColor('#172535'),spaceAfter=7),
 'small':ParagraphStyle('small',fontName='CV',fontSize=8.5,leading=12,textColor=HexColor('#556475'),spaceAfter=6)
}
items=[('name','Denis Gruszkiewicz'),('title','Przekładnia cykloidalna | przykład projektu CAD'),('small','Załącznik do aplikacji na stanowisko Młodszy Konstruktor w Greenbrier Poland'),('body','Projekt własny przedstawiający modelowanie elementów przekładni i ich współpracę w złożeniu. Wybrany arkusz pokazuje wewnętrzny układ mechanizmu, oznaczenia części oraz zestawienie elementów.'),('head','ZAKRES PRACY'),('body','Opracowanie geometrii przekładni i modelowanie części mechanicznych; analiza zasady działania, współpracy elementów oraz zagadnień montażu. Przygotowanie graficznej prezentacji konstrukcji w postaci rysunku złożeniowego.'),('head','CO PRZEDSTAWIA ZAŁĄCZONY RYSUNEK'),('body','Przekrój przez zespół oraz widok poprzeczny mechanizmu. Na arkuszu wskazano m.in. koła cykloidalne, tarcze wyjściowe, wał wejściowy, korpus, łożyska i elementy złączne. Zestawienie części pozwala powiązać oznaczenia na rysunku z elementami zespołu.'),('head','PODGLĄD ARKUSZA')]
story=[Paragraph(t,styles[k]) for k,t in items]
story += [Image(str(root/'tmp/pdfs/cyclo-fixed.png'),width=510,height=360),Spacer(1,7),Paragraph('Dalej zamieszczono 7 arkuszy: złożenie oraz rysunki wału wejściowego, koła cykloidalnego, korpusu, mocowania, tarczy wyjściowej i sworznia. Rysunki zawierają wymiary, wybrane pasowania, tolerancje i oznaczenia chropowatości.',styles['small']),Paragraph('Na oryginalnym arkuszu widnieje wcześniejszy zapis imienia i nazwiska autora: Denys Hrushkevych. W aplikacji używam nazwiska Denis Gruszkiewicz.',styles['small']),Paragraph('Kontakt: r3dflzp.ns@gmail.com | +48 511 592 887',styles['small'])]
cover=root/'tmp/pdfs/cyclo-intro.pdf'
SimpleDocTemplate(str(cover),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=30,bottomMargin=30,title='Denis Gruszkiewicz - Przekładnia cykloidalna').build(story)
assert len(PdfReader(cover).pages)==1
w=PdfWriter();w.append(str(cover));w.append('C:/Users/r3d_flzp/Downloads/cykloidalna_fixed.pdf');w.add_metadata({'/Title':'Denis Gruszkiewicz - Przekładnia cykloidalna - portfolio CAD','/Author':'Denis Gruszkiewicz'})
out=root/'output/pdf/Denis_Gruszkiewicz_Cycloidal_Drive_Portfolio_PL.pdf'
w.write(str(out));assert len(PdfReader(out).pages)==8
print('Portfolio: 8 pages;',out.stat().st_size,'bytes')
message='''Szanowni Państwo,

chciałbym zgłosić swoją kandydaturę na stanowisko Młodszego Konstruktora w Greenbrier Poland. Studiuję Robotykę i Automatyzację Procesów na Politechnice Wrocławskiej; ukończyłem V semestr i kontynuuję studia inżynierskie.

Rozwijam własne projekty mechaniczne, korzystając z Fusion 360 i AutoCAD. W załączeniu przesyłam CV oraz przykład mojego projektu przekładni cykloidalnej z rysunkiem złożeniowym i rysunkami wykonawczymi części. Pracując nad nim, zajmowałem się geometrią części, ich współpracą w złożeniu i zagadnieniami montażu.

Zależy mi na rozpoczęciu pracy konstruktorskiej i rozwijaniu umiejętności modelowania 3D oraz przygotowywania dokumentacji technicznej pod opieką doświadczonego zespołu. Jestem gotowy poznawać normy i specyfikę branży kolejowej. Posługuję się angielskim technicznym, bardzo dobrze znam MS Office i posiadam prawo jazdy kat. B.

Będę wdzięczny za rozważenie mojej kandydatury również na obecnym etapie studiów. Chętnie opowiem o projekcie oraz omówię możliwość współpracy.

Z poważaniem,
Denis Gruszkiewicz
+48 511 592 887
r3dflzp.ns@gmail.com
'''
(root/'output/Greenbrier_message_PL.txt').write_text(message,encoding='utf-8')




======== FILE: build_draco.py ========

from pathlib import Path
from xml.sax.saxutils import escape
import json
from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
root=Path(__file__).resolve().parent
out=root/'output/pdf'
pdfmetrics.registerFont(TTFont('CV','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('CVB','C:/Windows/Fonts/arialbd.ttf'))
styles={}
for kind,font,size,leading,before,after in [('name','CVB',25,29,0,5),('role','CVB',11,15,0,6),('contact','CV',9,12,0,3),('section','CVB',10,13,10,5),('title','CVB',9.5,13,0,3),('body','CV',9.3,12.7,0,4),('bullet','CV',9.3,12.7,0,3)]:
 styles[kind]=ParagraphStyle(kind,fontName=font,fontSize=size,leading=leading,spaceBefore=before,spaceAfter=after,textColor=HexColor('#17617A' if kind in ['role','section'] else '#172535'),leftIndent=8 if kind=='bullet' else 0,firstLineIndent=-8 if kind=='bullet' else 0)
blocks=[
('name','Denis Gruszkiewicz'),
('role','Młodszy Specjalista ds. Wsparcia IT i Administracji Systemami'),
('contact','Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com'),
('contact','Prawo jazdy kat. B od 3 lat | Gotowość do wizyt i dyżurów u klientów'),
('section','PROFIL ZAWODOWY'),
('body','Młodszy Administrator IT z ponad rokiem doświadczenia w szpitalu. Wspieram użytkowników, diagnozuję problemy sprzętowe, systemowe i aplikacyjne oraz konfiguruję stanowiska i urządzenia sieciowe. Bardzo dobrze znam Microsoft 365, mam praktykę w dołączaniu komputerów do domeny i podstawy pracy z Linuxem. Chcę wykorzystać to doświadczenie w DRACO i rozwijać administrację systemami przy wsparciu bardziej doświadczonego administratora.'),
('section','KLUCZOWE KOMPETENCJE'),
('bullet','Windows i sprzęt PC: diagnozowanie problemów, konfiguracja stanowisk, składanie, modernizacja i serwis komputerów.'),
('bullet','Microsoft 365 - bardzo dobra znajomość pakietu; wsparcie użytkowników w codziennej pracy z aplikacjami.'),
('bullet','Active Directory - podstawowy zakres praktyczny: dołączanie komputerów do domeny.'),
('bullet','Sieci: okablowanie LAN, podłączanie switchy i urządzeń, podstawy DHCP i routingu oraz diagnostyka połączeń.'),
('bullet','Linux - podstawowa administracja i diagnostyka; testowanie działania aplikacji, odtwarzanie błędów i walidacja danych.'),
('section','DOŚWIADCZENIE ZAWODOWE'),
('title','Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie'),
('bullet','Bieżące wsparcie techniczne pracowników: rozpoznawanie problemów sprzętowych, systemowych i aplikacyjnych oraz pomoc w ich rozwiązaniu.'),
('bullet','Podłączanie i konfiguracja stanowisk, switchy i urządzeń sieciowych; prowadzenie okablowania LAN i podstawowa diagnostyka połączeń.'),
('bullet','Analiza potrzeb użytkowników i rozwój wewnętrznych narzędzi upraszczających powtarzalne czynności.'),
('bullet','Testowanie scenariuszy, odtwarzanie zgłaszanych błędów i poprawianie aplikacji na podstawie potrzeb pracowników.'),
('section','PROJEKTY I AUTOMATYZACJA'),
('body','LabFlow: demonstracyjna aplikacja Django/React do koordynacji procesów laboratoryjnych, z rolami użytkowników i audytem; dokumentacja konfiguracji Windows/Ubuntu oraz backupu i odtwarzania. JobHunter: automatyzacja workflow z n8n, PostgreSQL i lokalną LLM; GitHub Actions CI. Python i narzędzia AI wykorzystuję do analizy kodu i prototypowania.'),
('contact','Portfolio techniczne: github.com/Flyingzaptop'),
('section','WYKSZTAŁCENIE'),
('title','WSB Merito we Wrocławiu | 03.2026 - obecnie'),
('body','Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr.'),
('title','Politechnika Wrocławska | 10.2022 - obecnie'),
('body','Robotyka i Automatyzacja Procesów, studia inżynierskie; ukończony V semestr.'),
('section','JĘZYKI I INFORMACJE DODATKOWE'),
('body','Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. Kurs IT Step Python AI: 02.2024 - 12.2024.'),
('body','Dodatkowe zaplecze: Fusion 360, AutoCAD, RobotStudio i własne projekty mechaniczne. Zainteresowanie pracą na część etatu lub pełny etat w modelu hybrydowym; termin rozpoczęcia do uzgodnienia.'),
]
def footer(c,d):
 c.setStrokeColor(HexColor('#D9E2E9'));c.line(42,36,A4[0]-42,36);c.setFont('CV',7);c.setFillColor(HexColor('#556475'));c.drawString(42,24,'Denis Gruszkiewicz | r3dflzp.ns@gmail.com');c.drawRightString(A4[0]-42,24,str(d.page))
story=[]
for kind,t in blocks:
 p=Paragraph(escape(('- ' if kind=='bullet' else '')+t),styles[kind]);p.keepWithNext=kind in ['title','section'];story.append(p)
path=out/'Denis_Gruszkiewicz_CV_DRACO_IT_Support_PL.pdf'
SimpleDocTemplate(str(path),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=32,bottomMargin=46,title='Denis Gruszkiewicz - IT Support - DRACO',author='Denis Gruszkiewicz').build(story,onFirstPage=footer,onLaterPages=footer)
(out/'DRACO_content.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
import pdfplumber,pypdfium2 as pdfium
with pdfplumber.open(path) as pdf:
 text=' '.join(p.extract_text() or '' for p in pdf.pages)
 assert all(s in text for s in ['r3dflzp.ns@gmail.com','kat. B','Microsoft 365','dołączanie komputerów do domeny','II semestr','V semestr'])
 assert 'Windows Server' not in text
 print('Pages:',len(pdf.pages),'Contact/skills/education checks: OK')
doc=pdfium.PdfDocument(str(path))
for i,p in enumerate(doc):p.render(scale=1.4).to_pil().save(root/f'tmp/pdfs/draco-{i+1}.png')



======== FILE: build_greenbrier.py ========

from pathlib import Path
exec((Path(__file__).parent/'build_draco.py').read_text(encoding='utf-8-sig').split('blocks=[')[0])
from reportlab.platypus import PageBreak
styles['body'].fontSize=10;styles['body'].leading=14
styles['bullet'].fontSize=10;styles['bullet'].leading=14
styles['section'].spaceBefore=11
blocks=[
('name','Denis Gruszkiewicz'),
('role','Młodszy Konstruktor | CAD 2D/3D, mechanika i prototypowanie'),
('contact','Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com'),
('contact','Prawo jazdy kat. B od 3 lat | github.com/Flyingzaptop - projekty IT i R&D'),
('section','PROFIL ZAWODOWY'),
('body','Student Robotyki i Automatyzacji Procesów na Politechnice Wrocławskiej, po ukończeniu V semestru. Rozwijam własne projekty mechaniczne i akademickie projekty robotyki, łącząc modelowanie 3D, rysunek techniczny i analizę współpracy elementów. Pracuję przede wszystkim w Fusion 360 i AutoCAD. Chcę wykorzystać tę podstawę na stanowisku Młodszego Konstruktora w Greenbrier, rozwijając umiejętność przygotowywania modeli, rysunków i dokumentacji oraz poznając normy branży kolejowej. Dodatkowym atutem jest doświadczenie zawodowe w diagnozowaniu problemów technicznych i testowaniu aplikacji.'),
('section','KOMPETENCJE KONSTRUKCYJNE'),
('bullet','Fusion 360 - główne środowisko modelowania 3D; części, złożenia i analiza geometrii konstrukcji.'),
('bullet','AutoCAD - rysunek 2D i dokumentacja techniczna; interpretacja rysunków oraz przestrzenne rozumienie konstrukcji.'),
('bullet','Projektowanie mechanizmów: analiza zasady działania, współpracy elementów, montażu, tolerancji i precyzji wykonania w projektach własnych.'),
('bullet','Prototypowanie: modele STEP/STL, przygotowanie elementów do druku 3D i uwzględnianie ograniczeń technologii FDM.'),
('bullet','Siemens NX i FluidSim - podstawy; RobotStudio - akademickie stanowiska spawania i paletyzacji.'),
('bullet','Podstawy projektowania maszyn, mechaniki, technologii materiałów i procesów obróbki rozwijane w ramach studiów.'),
('section','WYBRANE PROJEKTY INŻYNIERSKIE'),
('title','Przekładnia cykloidalna | projekt własny'),
('bullet','Projektowanie geometrii przekładni oraz modelowanie części mechanicznych.'),
('bullet','Analiza zasady działania i współpracy elementów mechanizmu, z uwzględnieniem montażu, tolerancji oraz praktycznego wykonania.'),
('title','Osiowy silnik odrzutowy | projekt koncepcyjny'),
('bullet','Samodzielne opracowanie koncepcji oraz modelowanie głównych elementów konstrukcyjnych w CAD.'),
('bullet','Analiza geometrii, układu przepływu i rozmieszczenia komponentów; wizualizacja rozwiązania technicznego.'),
('title','RobotStudio | projekty akademickie'),
('bullet','Projektowanie stanowisk zrobotyzowanych dla procesów spawania i paletyzacji.'),
('bullet','Analiza trajektorii, zasięgu robota, organizacji stanowiska i logiki kolejnych etapów procesu.'),
('title','Druk 3D i prototypowanie | projekty własne'),
('body','Projektowanie elementów pod druk 3D i praca z modelami STEP/STL. Uwzględnianie ograniczeń FDM oraz praktyczne podejście do montażu, testowania i poprawiania konstrukcji.'),
('page',''),
('section','WYKSZTAŁCENIE'),
('title','Politechnika Wrocławska | 10.2022 - obecnie'),
('body','Robotyka i Automatyzacja Procesów, studia inżynierskie w toku; ukończony V semestr.'),
('bullet','Zakres: mechanika, fizyka techniczna, matematyka inżynierska, rysunek techniczny, CAD, projektowanie maszyn, automatyka i robotyka przemysłowa.'),
('bullet','Projekty i zajęcia związane ze stanowiskami zrobotyzowanymi, spawaniem, paletyzacją, obróbką materiałów i symulacją układów.'),
('title','Uniwersytet WSB Merito we Wrocławiu | 03.2026 - obecnie'),
('body','Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr. Rozwijanie kompetencji informatycznych wspierających analizę danych i pracę z systemami technicznymi.'),
('section','DOŚWIADCZENIE ZAWODOWE'),
('title','Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie'),
('bullet','Bieżące wsparcie techniczne pracowników oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych.'),
('bullet','Analiza potrzeb użytkowników, odtwarzanie błędów i testowanie scenariuszy działania narzędzi.'),
('bullet','Rozwój wewnętrznych aplikacji usprawniających pracę: oddzielne projekty zarządzania pracownikami, grafikiem i procesami laboratoryjnymi.'),
('bullet','Podłączanie i konfiguracja stanowisk oraz urządzeń sieciowych, okablowanie LAN i podstawowa diagnostyka połączeń.'),
('section','DODATKOWE PROJEKTY I UMIEJĘTNOŚCI TECHNICZNE'),
('title','Analiza danych i programowanie'),
('body','Python, NumPy i Pandas; własne badania danych czasowych i modeli ML. Pozyskiwanie i przygotowanie danych, projektowanie metryk, porównywanie eksperymentów oraz analiza błędów i ograniczeń wyników.'),
('title','LabFlow i ARC | projekty software / R&D'),
('body','LabFlow: demonstracyjna aplikacja Django/React odwzorowująca wieloetapowy proces laboratoryjny, z rolami, walidacją i audytem. ARC: eksperymentalny runtime C++/D3D12, analiza zasobów, zależności i wydajności oraz testy. Projekty rozwijają systemowe podejście do problemów i weryfikacji rozwiązań.'),
('body','Bardzo dobra znajomość Microsoft 365 / MS Office, w tym Excel i PowerPoint. Diagnostyka, składanie i modernizacja komputerów PC, także konfiguracji hard-tube water cooling. Współtworzenie inicjatywy Antillia związanej z aplikacjami i automatyzacją.'),
('section','KURSY, JĘZYKI I INFORMACJE DODATKOWE'),
('body','IT Step - Python AI | 02.2024 - 12.2024; kurs programowania w Pythonie i sztucznej inteligencji.'),
('body','Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste.'),
('body','Prawo jazdy kat. B od 3 lat. Miejsce zamieszkania: Wrocław. Termin rozpoczęcia pracy do uzgodnienia.'),
]
def footer(c,d):
 c.setStrokeColor(HexColor('#D9E2E9'));c.line(42,36,A4[0]-42,36);c.setFont('CV',7);c.setFillColor(HexColor('#556475'));c.drawString(42,24,'Denis Gruszkiewicz | r3dflzp.ns@gmail.com');c.drawRightString(A4[0]-42,24,str(d.page))
story=[]
for kind,t in blocks:
 if kind=='page':story.append(PageBreak());continue
 p=Paragraph(escape(('- ' if kind=='bullet' else '')+t),styles[kind]);p.keepWithNext=kind in ['title','section'];story.append(p)
path=out/'Denis_Gruszkiewicz_CV_Greenbrier_Mlodszy_Konstruktor_PL.pdf'
SimpleDocTemplate(str(path),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=30,bottomMargin=47,title='Denis Gruszkiewicz - Młodszy Konstruktor - Greenbrier',author='Denis Gruszkiewicz').build(story,onFirstPage=footer,onLaterPages=footer)
(out/'Greenbrier_content.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
(root/'output/Greenbrier_CV_text_PL.txt').write_text('\n\n'.join(t for k,t in blocks if k!='page'),encoding='utf-8')
import pdfplumber,pypdfium2 as pdfium
with pdfplumber.open(path) as pdf:
 t=' '.join(p.extract_text() or '' for p in pdf.pages)
 assert all(s in t for s in ['r3dflzp.ns@gmail.com','studia inżynierskie w toku','V semestr','II semestr','kat. B','Greenbrier'])
 assert 'flyingzaptop@gmail.com' not in t
 for p in pdf.pages: assert all(0<=c['x0']<c['x1']<=p.width+.1 for c in p.chars)
 print('Pages:',len(pdf.pages),'Text and page bounds: OK')
doc=pdfium.PdfDocument(str(path))
for i,p in enumerate(doc):p.render(scale=1.4).to_pil().save(root/f'tmp/pdfs/greenbrier-{i+1}.png')



======== FILE: build_opera.py ========

from pathlib import Path
exec((Path(__file__).parent/'build_draco.py').read_text(encoding='utf-8-sig').split('blocks=[')[0])
from reportlab.platypus import PageBreak
styles['body'].fontSize=10;styles['body'].leading=14
styles['bullet'].fontSize=10;styles['bullet'].leading=14
blocks=[
('name','Denis Gruszkiewicz'),
('role','AI / ML Engineering | Python, neural networks and experimental research'),
('contact','Wrocław, Poland | +48 511 592 887 | r3dflzp.ns@gmail.com'),
('contact','GitHub: github.com/Flyingzaptop'),
('section','PROFILE'),
('body','Engineering student and Junior IT Administrator with multi-year independent research in financial time series and neural networks. I build data pipelines, design features and training targets, compare model architectures and investigate failure modes. My projects combine Python/PyTorch, causal validation and reproducible experiments with local LLM integrations and application development. I am interested in contributing this research and software foundation to Opera’s AI team in Wrocław.'),
('section','CORE SKILLS'),
('bullet','Python, PyTorch, NumPy, Pandas, Polars and PyArrow/Parquet; Jupyter/Colab and Matplotlib for analysis and visualization.'),
('bullet','Neural sequence modeling: TCN, LSTM and RetNet-lite; feature/label design, custom losses, checkpointing and evaluation.'),
('bullet','Experimental methods: chronological validation, data-leakage checks, baseline comparisons, error analysis and interpretation of negative results.'),
('bullet','LLM applications: local Ollama/LM Studio, OpenAI API integration and academic Hugging Face Transformers text-generation practice.'),
('bullet','Software: Django REST Framework, REST APIs, PostgreSQL/SQLite, basic SQL, React/TypeScript; GitHub Actions, pytest and native Rust/PyO3 components.'),
('section','SELECTED MACHINE LEARNING RESEARCH'),
('title','XAUUSD angular sequence research | independent project'),
('bullet','Implemented experimental PyTorch TCN models and an asynchronous event branch with learned attention pooling, custom losses and geometric output constraints.'),
('bullet','Investigated chronological forecasting, distillation and reconstruction as separate tasks; used causality tests and controlled baseline comparisons.'),
('body','github.com/Flyingzaptop/xauusd'),
('title','stargazin | sequence models and offline/online consistency'),
('bullet','Built a pipeline covering Parquet ingestion, normalization, features, labels, dataset assembly, training/checkpointing and offline scoring.'),
('bullet','Explored CT-LSTM and RetNet-lite variants, three-class output heads and margin objectives; investigated unstable predictions and preprocessing consistency.'),
('bullet','Used Rust/PyO3 extensions for selected preprocessing paths and maintained unit, integration and regression tests.'),
('body','github.com/Flyingzaptop/stargazin'),
('page',''),
('section','DATA QUALITY AND EXPERIMENT VALIDATION'),
('title','GC MBO research | event-level market-data experiments'),
('bullet','Python feature engineering and model experiments on CME Gold MBO/L3 data; Rust replay and conservative FIFO execution simulation.'),
('bullet','Evaluated hypotheses using walk-forward analysis, causality checks and execution-cost/latency stress. Documented failed hypotheses and limits rather than treating backtests as proof of a usable strategy.'),
('body','github.com/Flyingzaptop/gc-mbo-research'),
('body','Additional practice: stargaze-l2-vwap - async collectors and recoverable Parquet storage; Python-Colab - scikit-learn preprocessing/regression, NLTK and TF-IDF/SVD/SVC text classification.'),
('section','LLM APPLICATIONS AND SOFTWARE PROJECTS'),
('title','JobHunter | structured LLM analysis and workflow automation'),
('body','Node.js/n8n, PostgreSQL, Ollama and Playwright; deterministic processing, schema-validated LLM analysis, React/SSE dashboard and human-in-the-loop controls. Docker Compose configuration and GitHub Actions CI. Local project under development: github.com/Flyingzaptop/jobhunter-n8n.'),
('title','LabFlow | process application and local AI integrations'),
('body','Django REST Framework + React/TypeScript, REST/OpenAPI, RBAC and audit logging. Implemented local Ollama streaming client and optional faster-whisper speech-to-text. Public demonstrator with fictional data: github.com/Flyingzaptop/LabFlow.'),
('body','ARC: experimental C++/D3D12 resource and performance research with CMake/CTest CI. MultiNeuro: Python Telegram bot using OpenAI API. Antillia: co-developing an early-stage web/software/AI initiative (antillia.tech).'),
('section','PROFESSIONAL EXPERIENCE'),
('title','Junior IT Administrator | ZOZ w Bolesławcu | 06.2025 - present'),
('bullet','Support staff, diagnose hardware/system/application issues and develop internal tools based on user needs.'),
('bullet','Test application scenarios, validate data, reproduce defects and improve application logic; separate projects for employee management, schedules and laboratory coordination.'),
('section','EDUCATION AND TRAINING'),
('title','Wrocław University of Science and Technology | 10.2022 - present'),
('body','Robotics and Process Automation, engineering studies; completed the fifth semester. Coursework includes engineering mathematics, physics, mechanics, automation and robotics.'),
('title','WSB Merito University in Wrocław | 03.2026 - present'),
('body','Network, Systems and IT Security Engineering; part-time studies, second semester.'),
('body','IT Step - Python AI, 02.2024 - 12.2024; Python and AI grades: 10/10 each.'),
('section','LANGUAGES AND ENGINEERING BACKGROUND'),
('body','Polish: advanced; English: advanced / technical; Ukrainian and Russian: native. CAD/robotics projects: Fusion 360, AutoCAD, RobotStudio, cycloidal drive, axial turbojet concept and 3D-printing components.'),
]
def footer(c,d):
 c.setStrokeColor(HexColor('#D9E2E9'));c.line(42,36,A4[0]-42,36);c.setFont('CV',7);c.setFillColor(HexColor('#556475'));c.drawString(42,24,'Denis Gruszkiewicz | r3dflzp.ns@gmail.com');c.drawRightString(A4[0]-42,24,str(d.page))
story=[]
for kind,t in blocks:
 if kind=='page':story.append(PageBreak());continue
 p=Paragraph(escape(('- ' if kind=='bullet' else '')+t),styles[kind]);p.keepWithNext=kind in ['title','section'];story.append(p)
path=out/'Denis_Gruszkiewicz_CV_Opera_AI_Engineer_EN.pdf'
SimpleDocTemplate(str(path),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=32,bottomMargin=46,title='Denis Gruszkiewicz - Opera AI Engineer',author='Denis Gruszkiewicz').build(story,onFirstPage=footer,onLaterPages=footer)
(out/'Opera_content.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
import pdfplumber,pypdfium2 as pdfium
with pdfplumber.open(path) as pdf:
 t=' '.join(p.extract_text() or '' for p in pdf.pages)
 assert all(s in t for s in ['r3dflzp.ns@gmail.com','fifth semester','second semester','PyTorch','Opera'])
 print('Pages:',len(pdf.pages),'Text QA OK')
doc=pdfium.PdfDocument(str(path))
for i,p in enumerate(doc):p.render(scale=1.2).to_pil().save(root/f'tmp/pdfs/opera-{i+1}.png')



======== FILE: build_opera_portfolio.py ========

from pathlib import Path
exec((Path(__file__).parent/'build_draco.py').read_text(encoding='utf-8-sig').split('blocks=[')[0])
styles['body'].fontSize=10;styles['body'].leading=14
styles['bullet'].fontSize=10;styles['bullet'].leading=14
blocks=[
('name','Denis Gruszkiewicz'),
('role','Selected ML Research & AI Projects'),
('contact','r3dflzp.ns@gmail.com | github.com/Flyingzaptop | Wrocław, Poland'),
('section','RESEARCH APPROACH'),
('body','My independent research has focused on financial time series. The transferable problems are broader: building reliable datasets, defining meaningful targets, preventing leakage, comparing architectures and understanding why a model fails. I use explicit baselines and causal tests, and document limitations alongside results.'),
('section','1. XAUUSD: NEURAL SEQUENCE EXPERIMENTS'),
('body','Explored angular representations, causal temporal convolutional networks and asynchronous event inputs with attention pooling in PyTorch. Separate experiments investigate forecasting and bidirectional reconstruction.'),
('bullet','Designed custom losses and output constraints; compared reconstruction approaches against interpolation baselines.'),
('bullet','Added causality checks to prevent future events entering forecasting inputs. Reconstruction results did not establish a clear advantage over the strong baseline.'),
('contact','https://github.com/Flyingzaptop/xauusd'),
('section','2. STARGAZIN: MODEL BEHAVIOR AND PIPELINE CONSISTENCY'),
('body','Built a pipeline from Parquet ingestion and normalization through features, labels, training/checkpoints and offline scoring. Explored CT-LSTM and RetNet-lite variants, output-head redesigns and margin objectives.'),
('bullet','Investigated collapsed or unstable predictions and consistency between offline and online preprocessing.'),
('bullet','Used Rust/PyO3 extensions for selected preprocessing paths, with unit, integration and regression tests.'),
('contact','https://github.com/Flyingzaptop/stargazin'),
('section','3. GC MBO RESEARCH: EVALUATION UNDER REALISTIC ASSUMPTIONS'),
('body','Investigated event-level gold-futures data using Python feature engineering and ML experiments, Rust replay and conservative FIFO execution simulation.'),
('bullet','Used walk-forward evaluation, causality checks and latency/cost stress to distinguish model signals from artifacts of the evaluation setup.'),
('bullet','The published research did not establish a stable executable trading edge. Its value lies in reusable infrastructure, explicit assumptions and documented rejected hypotheses.'),
('contact','https://github.com/Flyingzaptop/gc-mbo-research'),
('section','FROM RESEARCH TO APPLICATIONS'),
('body','JobHunter combines local LLM analysis, deterministic validation, n8n/Node.js workflows, PostgreSQL and human review. LabFlow is a Django/React demonstrator with RBAC, audit history, a local Ollama streaming client and optional faster-whisper speech-to-text.'),
('contact','https://github.com/Flyingzaptop/jobhunter-n8n | https://github.com/Flyingzaptop/LabFlow'),
('section','CONTEXT'),
('body','These are independent and academic projects, alongside my work as a Junior IT Administrator. I am studying Robotics and Process Automation (five semesters completed) and IT systems/network engineering. Code, methodology and documented results are available in the repositories; full reproduction can require local datasets, model checkpoints or suitable hardware.'),
]
story=[]
for kind,t in blocks:
 p=Paragraph(escape(('- ' if kind=='bullet' else '')+t),styles[kind]);p.keepWithNext=kind in ['title','section'];story.append(p)
path=out/'Denis_Gruszkiewicz_Opera_Research_Portfolio_EN.pdf'
SimpleDocTemplate(str(path),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=30,bottomMargin=32,title='Denis Gruszkiewicz - Selected ML Research and AI Projects',author='Denis Gruszkiewicz').build(story)
import pdfplumber,pypdfium2 as pdfium
with pdfplumber.open(path) as d:
 assert len(d.pages)==1,len(d.pages)
 print('One-page portfolio: text extraction OK')
doc=pdfium.PdfDocument(str(path));doc[0].render(scale=1.4).to_pil().save(root/'tmp/pdfs/opera-portfolio.png')



======== FILE: build_selected_three.py ========

from pathlib import Path
exec((Path(__file__).parent/'build_draco.py').read_text(encoding='utf-8-sig').split('blocks=[')[0])
import pdfplumber,pypdfium2 as pdfium
styles['section'].spaceBefore=8
styles['body'].leading=12.2
styles['bullet'].leading=12.2
contact=[('name','Denis Gruszkiewicz'),('contact','Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com')]
edupl=[('section','WYKSZTAŁCENIE'),('title','WSB Merito we Wrocławiu | 03.2026 - obecnie'),('body','Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr.'),('title','Politechnika Wrocławska | 10.2022 - obecnie'),('body','Robotyka i Automatyzacja Procesów; studia inżynierskie w toku, ukończony V semestr.')]
endpl=[('section','JĘZYKI I DOSTĘPNOŚĆ'),('body','Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. Prawo jazdy kat. B. IT Step: Python AI, 02.2024 - 12.2024.'),('body','Elastyczne godziny pracy; możliwa część etatu. Od marca 2027 maksymalnie 1-2 dni w tygodniu stacjonarnie we Wrocławiu, pozostała praca zdalnie. Termin rozpoczęcia do uzgodnienia.')]
dcg=[contact[0],('role','Młodszy Specjalista Bezpieczeństwa IT | wsparcie IT i diagnostyka'),contact[1],('contact','Portfolio techniczne: github.com/Flyingzaptop'),('section','PROFIL ZAWODOWY'),('body','Młodszy Administrator IT z ponad rokiem doświadczenia we wsparciu pracowników szpitala. Diagnozuję problemy sprzętowe, systemowe i aplikacyjne, odtwarzam błędy oraz weryfikuję poprawki. Studiuję inżynierię sieci, systemów i bezpieczeństwa IT. Chcę wykorzystać doświadczenie w obsłudze problemów użytkowników i analizie danych w zespole bezpieczeństwa DCG, rozwijając kompetencje w analizie alertów SIEM, EDR/XDR i DLP.'),('section','KOMPETENCJE PRZYDATNE W OPERACJACH BEZPIECZEŃSTWA'),('bullet','Diagnostyka: zbieranie informacji o problemie, odtwarzanie błędów, weryfikacja działania aplikacji i poprawności danych.'),('bullet','Windows i sprzęt PC: konfiguracja stanowisk, rozwiązywanie problemów systemowych, modernizacja i serwis komputerów.'),('bullet','Sieci: okablowanie LAN, podłączanie switchy i urządzeń, podstawy DHCP i routingu oraz diagnostyka połączeń.'),('bullet','Linux - podstawowa administracja i diagnostyka. Active Directory - dołączanie komputerów do domeny. Microsoft 365 - bardzo dobra znajomość pakietu.'),('bullet','Python, podstawy SQL, PostgreSQL/SQLite; Git/GitHub, testowanie aplikacji i automatyzacja workflow w projektach własnych.'),('section','DOŚWIADCZENIE ZAWODOWE'),('title','Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie'),('bullet','Bieżące wsparcie techniczne pracowników oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych.'),('bullet','Konfiguracja stanowisk i urządzeń sieciowych, okablowanie LAN oraz podstawowa diagnostyka połączeń.'),('bullet','Analiza potrzeb użytkowników, odtwarzanie zgłaszanych błędów, testowanie scenariuszy i sprawdzanie poprawności danych.'),('bullet','Rozwój wewnętrznych narzędzi usprawniających powtarzalne czynności; oddzielne aplikacje dla pracowników, grafików i procesów laboratoryjnych.'),('section','PROJEKTY TECHNICZNE'),('title','LabFlow | role użytkowników, walidacja i historia operacji'),('body','Demonstracyjny system Django/React do koordynacji procesów laboratoryjnych. Role i uprawnienia użytkowników, audyt operacji, PostgreSQL/SQLite oraz testowanie reguł aplikacji. Dokumentacja konfiguracji Windows/Ubuntu, backupu i odtwarzania.'),('title','JobHunter | automatyzacja i kontrola jakości danych'),('body','n8n, PostgreSQL, lokalna LLM, Playwright i panel React. Deterministyczne przetwarzanie danych, walidacja wyników, testy oraz GitHub Actions CI. Praktyka analizowania problemów na styku kilku usług.'),('body','Dodatkowe zaplecze inżynierskie: Fusion 360, AutoCAD i RobotStudio; projekt przekładni cykloidalnej.')]+edupl+endpl
iclan=[contact[0],('role','Konstruktor CAD 3D / dokumentacja 2D | Fusion 360 i AutoCAD'),contact[1],('contact','Projekty mechaniczne: przekładnia cykloidalna, prototypowanie FDM'),('section','PROFIL ZAWODOWY'),('body','Student Robotyki i Automatyzacji Procesów na Politechnice Wrocławskiej, po ukończeniu V semestru. Modeluję części i złożenia w Fusion 360, pracuję z AutoCAD oraz rozwijam dokumentację techniczną własnych projektów. Projekt przekładni cykloidalnej obejmuje rysunek złożeniowy, zestawienie części i rysunki elementów. Chcę wykorzystać to zaplecze w iClan3D przy modelowaniu 3D i przygotowywaniu dokumentacji 2D oraz rozwijać pracę w Inventor i Navisworks.'),('section','KOMPETENCJE CAD I DOKUMENTACJA'),('bullet','Fusion 360 - modelowanie części i złożeń, analiza geometrii oraz współpracy elementów konstrukcji.'),('bullet','AutoCAD - rysunek 2D i dokumentacja techniczna; czytanie rysunków i przestrzenna interpretacja konstrukcji.'),('bullet','Rysunki części i złożenia: wymiary, przekroje, oznaczenia elementów i zestawienie części; wybrane pasowania, tolerancje i chropowatość w projekcie przekładni.'),('bullet','STEP/STL, przygotowanie modeli pod druk 3D; uwzględnianie ograniczeń FDM, montażu i praktycznego wykonania.'),('bullet','Podstawy mechaniki, konstrukcji maszyn, materiałów i procesów obróbki ze studiów. Siemens NX - podstawy; RobotStudio - projekty akademickie.'),('section','WYBRANE PROJEKTY INŻYNIERSKIE'),('title','Cyclo - przekładnia cykloidalna | projekt własny'),('bullet','Opracowanie geometrii i modelowanie części przekładni; analiza zasady działania, współpracy elementów i zagadnień montażu.'),('bullet','Dokumentacja obejmująca 7 arkuszy: złożenie oraz wał wejściowy, koło cykloidalne, korpus, mocowanie, tarczę wyjściową i sworzeń.'),('bullet','Przekroje, oznaczenia części i zestawienie elementów zespołu; wymiary oraz wybrane pasowania, tolerancje i oznaczenia chropowatości.'),('title','Osiowy silnik odrzutowy | projekt koncepcyjny'),('body','Koncepcja i modele głównych elementów konstrukcyjnych; analiza geometrii, układu przepływu i rozmieszczenia komponentów.'),('title','RobotStudio i prototypowanie FDM'),('body','Akademickie stanowiska spawania i paletyzacji: trajektorie, zasięg robota i organizacja procesu. Własne elementy pod druk 3D oraz praca z modelami STEP/STL.'),('section','DOŚWIADCZENIE I DODATKOWE UMIEJĘTNOŚCI'),('title','Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie'),('body','Wsparcie użytkowników, diagnozowanie usterek, testowanie aplikacji i rozwój wewnętrznych narzędzi. Praktyka samodzielnego rozwiązywania problemów technicznych i analizy potrzeb użytkowników.'),('body','Python, NumPy/Pandas, podstawy SQL; bardzo dobra znajomość Microsoft 365. LabFlow - aplikacja procesowa; JobHunter - automatyzacja workflow. Portfolio software: github.com/Flyingzaptop.')]+[edupl[0],edupl[3],edupl[4],edupl[1],edupl[2]]+endpl
story=[contact[0],('role','CAD Evaluation Engineer | CAD, Python and experimental validation'),contact[1],('contact','Software and ML portfolio: github.com/Flyingzaptop'),('section','PROFILE'),('body','Engineering student combining mechanical CAD projects with Python/ML research and automated testing. I model parts and assemblies in Fusion 360, prepare technical drawings and investigate how models and software behave under controlled tests. My work spans a cycloidal drive, neural time-series experiments and application automation. I want to contribute this combination to StoryGold’s CAD evaluation workflows. Engineering degree in progress; five semesters completed.'),('section','RELEVANT SKILLS'),('bullet','CAD: Fusion 360 part and assembly modeling; AutoCAD 2D drawings; STEP/STL workflows and FDM-aware prototyping. Basic Siemens NX.'),('bullet','Mechanical foundations: geometry, assembly relationships, dimensional tolerances and fits in personal projects; mechanics and machine-design coursework.'),('bullet','Python, PyTorch, NumPy and Pandas; data preparation, custom metrics, baseline comparisons and error analysis in independent ML research.'),('bullet','Validation: automated tests, reproducible experiments, chronological evaluation and data-leakage checks; Git/GitHub and CI workflows.'),('bullet','Software tools: C++/CMake/CTest, PostgreSQL/SQLite, Django/React, n8n and local LLM integration through Ollama.'),('section','CAD AND ENGINEERING PROJECTS'),('title','Cyclo - cycloidal drive | personal mechanical design project'),('body','Developed drive geometry and mechanical component models; examined component interaction and assembly. Prepared a seven-sheet drawing package covering the assembly and six components, with sections, a parts list, dimensions and selected fits, tolerances and surface-finish symbols.'),('title','Axial turbojet concept and RobotStudio projects'),('body','Conceptual CAD modeling of main engine components and their arrangement. Academic robotic welding and palletizing cells: trajectories, reach and process sequence. Additional FDM component designs and STEP/STL model preparation.'),('section','PYTHON, ML AND TESTING PROJECTS'),('title','XAUUSD / stargazin / GC MBO research | independent projects'),('body','Built Python data and model pipelines, including PyTorch sequence models, feature/target design, training and scoring. Used baseline comparisons, chronological validation, causality checks and analysis of failed hypotheses. This provides practical experience defining evaluation criteria and investigating failure modes.'),('title','ARC - Adaptive Runtime Core | C++ / D3D12'),('body','Experimental resource and performance research with CMake/CTest, automated regression testing and cross-platform CI builds. Analysed dependencies and runtime behaviour while developing testable software components.'),('title','JobHunter and LabFlow | application validation and automation'),('body','JobHunter combines n8n, PostgreSQL, Ollama, Playwright and React with schema validation, automated tests and GitHub Actions. LabFlow is a Django/React laboratory workflow demonstrator with user roles, audit history and data validation.'),('section','PROFESSIONAL EXPERIENCE'),('title','Junior IT Administrator | ZOZ w Bolesławcu | 06.2025 - present'),('body','Support hospital staff, troubleshoot hardware/system/application issues, reproduce reported defects and test application scenarios. Develop internal tools based on user needs, including separate employee-management, scheduling and laboratory-process projects.'),('section','EDUCATION AND LANGUAGES'),('body','Politechnika Wrocławska | Robotics and Process Automation | 10.2022 - present. Engineering studies in progress; five semesters completed. WSB Merito Wrocław | Network, Systems and IT Security Engineering | 03.2026 - present; part-time studies, second semester.'),('body','IT Step Python AI course, 02.2024 - 12.2024. English and Polish - advanced / technical; Ukrainian and Russian - native.'),('section','AVAILABILITY'),('body','Seeking remote work with flexible hours; open to part-time arrangements. From March 2027, onsite availability is limited to 1-2 days per week in Wrocław. Start date by agreement.')]
for key,blocks in [('DCG_Security_PL',dcg),('iClan3D_CAD_PL',iclan),('StoryGold_CAD_Evaluation_EN',story)]:
 if key.startswith('StoryGold'):
  styles['section'].spaceBefore=6
  styles['body'].leading=11.6
  styles['body'].spaceAfter=3
  styles['bullet'].leading=11.6
  styles['bullet'].spaceAfter=2
 storyflow=[]
 for kind,t in blocks:
  p=Paragraph(escape(('- ' if kind=='bullet' else '')+t),styles[kind]);p.keepWithNext=kind in ['title','section'];storyflow.append(p)
 path=out/f'Denis_Gruszkiewicz_CV_{key}.pdf'
 SimpleDocTemplate(str(path),pagesize=A4,leftMargin=40,rightMargin=40,topMargin=25,bottomMargin=26,title=f'Denis Gruszkiewicz - {key}',author='Denis Gruszkiewicz').build(storyflow)
 (out/f'{key}_content.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
 with pdfplumber.open(path) as doc:
  t=' '.join(p.extract_text() or '' for p in doc.pages)
  assert 'r3dflzp.ns@gmail.com' in t and '2027' in t
  print(key,'pages:',len(doc.pages))
  assert len(doc.pages)==1,(key,len(doc.pages))
  for page in doc.pages:assert all(0<=c['x0']<c['x1']<=page.width+.1 for c in page.chars)
 doc=pdfium.PdfDocument(str(path))
 for i,p in enumerate(doc):p.render(scale=1.5).to_pil().save(root/f'tmp/pdfs/{key}-{i+1}.png')



======== FILE: build_storygold_focused.py ========

from pathlib import Path
exec((Path(__file__).parent/'build_draco.py').read_text(encoding='utf-8-sig').split('blocks=[')[0])
from reportlab.platypus import PageBreak,Image,Spacer
import pdfplumber,pypdfium2 as pdfium
styles['body'].fontSize=9.7;styles['body'].leading=13
styles['bullet'].fontSize=9.7;styles['bullet'].leading=13
styles['section'].spaceBefore=8
styles['caption']=ParagraphStyle('caption',fontName='CV',fontSize=7.8,leading=10,textColor=HexColor('#556475'),spaceAfter=5)
blocks=[
('name','Denis Gruszkiewicz'),
('role','CAD Evaluation Engineer | Mechanical design, FEA / CFD and Python / ML'),
('contact','Wrocław, Poland | +48 511 592 887 | r3dflzp.ns@gmail.com'),
('contact','GitHub: github.com/Flyingzaptop'),
('section','PROFILE AND MOTIVATION'),
('body','Engineering student with hands-on projects in mechanical CAD, centrifugal-force FEA and basic supersonic CFD, complemented by Python/PyTorch research and automated testing. My work includes an axial turbojet engine, a cycloidal drive and a RAMJET prototype project. StoryGold is a top-priority opportunity because it connects this mechanical-design foundation with my experience defining metrics, investigating failures and building repeatable model evaluations.'),
('section','CAD AND ENGINEERING FOUNDATION'),
('body','Fusion 360: parts and assemblies. AutoCAD: 2D technical documentation. Geometry, assembly relationships, dimensions, fits and tolerances; STEP/STL and FDM-aware design. Basic Siemens NX; academic RobotStudio welding and palletizing cells.'),
('section','SELECTED MECHANICAL DESIGN AND SIMULATION PROJECTS'),
('title','Axial Turbojet Engine | CAD and centrifugal-force FEA'),
('body','Developed the engine concept and CAD models of its main components, considering geometry and component arrangement. Used finite element analysis to investigate centrifugal loading within the project, connecting mechanical design with structural analysis.'),
('title','RAMJET Engine Prototype | basic Mach 2+ CFD simulation'),
('body','Worked on a RAMJET engine prototype project with basic CFD simulation of Mach 2+ flow. Combined design work with an introductory computational investigation of supersonic flow behaviour.'),
('title','Cyclo | cycloidal drive and technical drawing package'),
('body','Developed mechanical component geometry and an assembly, examining how the parts interact and fit together. Prepared seven drawing sheets: the assembly, input shaft, cycloidal disc, housing, mount, output disc and pin. Documentation includes sections, a parts list, dimensions and selected fits, tolerances and surface-finish symbols.'),
('image','cyclo-fixed.png'),
('caption','Example from my Cyclo drawing package: assembly sections and component references. The original title block uses my earlier name spelling, Denys Hrushkevych.'),
('body','Contribution to StoryGold: mechanical context for inspecting CAD geometry and constraints, plus Python and testing experience for benchmark tasks, automated scoring and failure analysis. I want to build on this foundation in CAD/CAE evaluation for AI-generated designs.'),
('page',''),
('section','PYTHON AND MACHINE LEARNING EVALUATION'),
('title','XAUUSD and stargazin | independent sequence-model research'),
('bullet','Built Python/PyTorch pipelines for data preparation, feature and target design, model training, checkpointing and scoring; explored TCN, CT-LSTM and RetNet-lite architectures.'),
('bullet','Compared models against baselines, tested chronological validity and data leakage, and investigated unstable predictions and preprocessing inconsistencies. Designed custom losses and evaluation metrics.'),
('contact','github.com/Flyingzaptop/xauusd | github.com/Flyingzaptop/stargazin'),
('title','GC MBO research | simulation and hypothesis testing'),
('body','Python feature engineering and model experiments on event-level market data, with Rust replay and conservative FIFO execution simulation. Used walk-forward evaluation, causality checks and cost/latency stress tests. Documented failed hypotheses and limitations to distinguish apparent performance from robust evidence.'),
('contact','github.com/Flyingzaptop/gc-mbo-research'),
('section','AUTOMATION AND REGRESSION TESTING'),
('title','ARC - Adaptive Runtime Core | C++ / CMake / CTest / D3D12'),
('body','Experimental runtime and resource-management research. Worked on automated regression tests and Windows/Linux CI builds across Debug/Release configurations, with GPU/runtime checks. Analysed dependencies, resource behaviour and performance to investigate failures systematically.'),
('title','JobHunter | LLM workflows with deterministic validation'),
('body','Built an automation platform using n8n, Node.js, PostgreSQL, Ollama, Playwright and Docker. Combined deterministic processing with schema-validated LLM analysis, a React/SSE dashboard, human-in-the-loop controls and GitHub Actions tests. This experience is directly useful when connecting model outputs to repeatable evaluation procedures.'),
('title','LabFlow | application logic, roles and auditability'),
('body','Django REST Framework and React/TypeScript laboratory workflow demonstrator with user roles, audit history, PostgreSQL/SQLite and validation of application rules. Prepared setup, backup and recovery documentation. Also co-developing Antillia, an early-stage software and automation initiative.'),
('section','PROFESSIONAL EXPERIENCE'),
('title','Junior IT Administrator | ZOZ w Bolesławcu | 06.2025 - present'),
('bullet','Provide technical support to hospital staff; diagnose hardware, Windows, connectivity and application issues, reproduce reported defects and verify fixes.'),
('bullet','Translate user needs into internal tools and test application workflows. Worked on separate employee-management, scheduling and laboratory-process applications.'),
('section','EDUCATION AND TECHNICAL FOUNDATION'),
('body','Politechnika Wrocławska | Robotics and Process Automation | 10.2022 - present. Engineering degree in progress; five semesters completed. Coursework in mechanics, engineering mathematics, physics, machine design, automation and robotics.'),
('body','WSB Merito Wrocław | Network, Systems and IT Security Engineering | 03.2026 - present; part-time studies, second semester. IT Step Python AI course | 02.2024 - 12.2024.'),
('body','Tools: Fusion 360, AutoCAD, basic Siemens NX, RobotStudio; Python, PyTorch, NumPy, Pandas, C++, Git/GitHub, CMake/CTest, PostgreSQL, Django, React and n8n.'),
('section','LANGUAGES AND WORKING ARRANGEMENTS'),
('body','English - advanced / technical; Polish - advanced; Ukrainian and Russian - native. Seeking remote work with flexible hours compatible with studies. From March 2027, onsite availability is limited to 1-2 days per week in Wrocław. Start date by agreement.')]
flow=[]
for k,t in blocks:
 if k=='page':flow.append(PageBreak());continue
 if k=='image':flow.append(Image(str(root/'tmp/pdfs'/t),width=354,height=250));continue
 p=Paragraph(escape(('- ' if k=='bullet' else '')+t),styles[k]);p.keepWithNext=k in ['section','title'];flow.append(p)
def foot(c,d):
 c.setFont('CV',7.5);c.setFillColor(HexColor('#556475'));c.drawString(40,21,'Denis Gruszkiewicz | StoryGold - CAD Evaluation Engineer');c.drawRightString(A4[0]-40,21,str(d.page))
path=out/'Denis_Gruszkiewicz_CV_StoryGold_CAD_Evaluation_EN.pdf'
SimpleDocTemplate(str(path),pagesize=A4,leftMargin=40,rightMargin=40,topMargin=28,bottomMargin=36,title='Denis Gruszkiewicz - StoryGold CAD Evaluation Engineer',author='Denis Gruszkiewicz').build(flow,onFirstPage=foot,onLaterPages=foot)
(out/'StoryGold_CAD_Evaluation_EN_content.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
with pdfplumber.open(path) as p:
 print('Pages:',len(p.pages))
 assert len(p.pages)==2
 t=' '.join(x.extract_text() or '' for x in p.pages)
 assert all(s in t for s in ['r3dflzp.ns@gmail.com','top-priority','degree in progress','March 2027','centrifugal-force FEA','Mach 2+','RAMJET','PyTorch'])
 for page in p.pages:assert all(0<=c['x0']<c['x1']<=page.width+.1 for c in page.chars)
doc=pdfium.PdfDocument(str(path))
for i,p in enumerate(doc):p.render(scale=1.4).to_pil().save(root/f'tmp/pdfs/storygold-focused-{i+1}.png')



======== FILE: build_support_four.py ========

from pathlib import Path
exec((Path(__file__).parent/'build_draco.py').read_text(encoding='utf-8-sig').split('blocks=[')[0])
import pdfplumber, pypdfium2 as pdfium
styles['section'].spaceBefore=8
styles['body'].leading=12.2
styles['bullet'].leading=12.2
configs={
'FOTC_EN': dict(en=True,role='Junior Cloud Support | IT troubleshooting and workflow automation',profile='Junior IT Administrator with over a year of hands-on experience supporting hospital staff, troubleshooting Windows, hardware and application issues, and configuring workstations. I combine user support with basic Linux and networking knowledge and practical web application projects. I want to bring this troubleshooting approach to FOTC and develop expertise in Google Workspace and SaaS support.',skills=[
'User support: understanding reported issues, reproducing errors, explaining solutions and checking that fixes work.',
'Windows and Microsoft 365: strong application familiarity and day-to-day user support; workstation setup and PC troubleshooting.',
'Networking: LAN cabling, connecting switches and devices, basic DHCP and routing concepts, connectivity troubleshooting.',
'Linux: basic administration and diagnostics. Active Directory: practical experience joining computers to a domain.',
'Automation and data: Python, n8n, PostgreSQL/SQLite, basic SQL; Git/GitHub and automated testing in personal projects.'],project='JobHunter - workflow automation',projecttext='Personal automation platform combining n8n, PostgreSQL, local LLM services, Playwright and a React dashboard. Worked with structured data, workflow validation, automated tests and GitHub Actions CI. This supports a systematic approach to investigating problems across connected services.'),
'CUI_PL':dict(en=False,role='Administrator IT | wsparcie aplikacji i systemów dziedzinowych',profile='Młodszy Administrator IT z ponad rokiem doświadczenia we wsparciu pracowników szpitala. Diagnozuję problemy aplikacyjne, systemowe i sprzętowe, odtwarzam błędy oraz testuję poprawki. Łączę kontakt z użytkownikami z projektową pracą nad aplikacjami Django/React i bazami danych. Chcę wykorzystać to zaplecze w CUI przy utrzymaniu aplikacji biznesowych, obsłudze zgłoszeń i rozwoju dokumentacji.',skills=[
'Wsparcie aplikacji: diagnozowanie problemów, odtwarzanie błędów, testowanie scenariuszy i weryfikacja poprawności danych.',
'Podstawy SQL; praktyka projektowa z PostgreSQL i SQLite oraz strukturą danych w aplikacjach.',
'Role i uprawnienia użytkowników, historia operacji i walidacja danych w projekcie LabFlow.',
'Windows, Microsoft 365 - bardzo dobra znajomość pakietu i wsparcie użytkowników; podstawy administracji i diagnostyki Linux.',
'Dokumentowanie konfiguracji i działania aplikacji; analiza potrzeb użytkowników, Python i automatyzacja powtarzalnych czynności.'],project='LabFlow | aplikacja procesowa Django / React',projecttext='Demonstracyjny system koordynacji procesów laboratoryjnych: etapy, statusy, formularze, role użytkowników i historia operacji. PostgreSQL/SQLite, testowanie reguł aplikacji oraz dokumentacja konfiguracji Windows/Ubuntu, backupu i odtwarzania. Projekt pokazuje umiejętność przekładania potrzeb użytkowników na działający system.'),
'BPX_PL':dict(en=False,role='Młodszy Specjalista IT | Windows, Linux i wsparcie użytkowników',profile='Młodszy Administrator IT z ponad rokiem doświadczenia w szpitalu. Wspieram użytkowników, konfiguruję stanowiska i diagnozuję problemy sprzętowe, aplikacyjne oraz sieciowe. Znam Windows, Microsoft 365 i podstawy Linuxa; rozwijam również aplikacje i automatyzacje. Chcę wykorzystać te umiejętności w BPX przy przygotowywaniu środowisk i wsparciu klientów oraz rozwijać administrację infrastrukturą pod okiem mentora.',skills=[
'Windows: konfiguracja stanowisk, instalacja aplikacji, diagnozowanie problemów oraz składanie, modernizacja i serwis komputerów.',
'Linux - podstawowa administracja i diagnostyka; projektowa dokumentacja uruchamiania aplikacji w Ubuntu.',
'Sieci: okablowanie LAN, podłączanie switchy i urządzeń, podstawy DHCP i routingu, diagnostyka połączeń.',
'Microsoft 365 - bardzo dobra znajomość pakietu. Active Directory - dołączanie komputerów do domeny.',
'Podstawy SQL, PostgreSQL/SQLite w projektach; Python, Git/GitHub, automatyzacja i testowanie aplikacji.'],project='LabFlow | konfiguracja i testowanie aplikacji',projecttext='Demonstracyjna aplikacja Django/React do koordynacji pracy laboratorium. Role użytkowników, walidacja danych i historia operacji; PostgreSQL/SQLite. Dokumentacja konfiguracji Windows/Ubuntu, backupu i odtwarzania oraz testowanie logiki procesu.'),
'Smith_Nephew_EN':dict(en=True,role='IT Service Desk Level 1 Intern | user support and troubleshooting',profile='Junior IT Administrator with over a year of experience supporting staff in a healthcare environment and a current part-time IT student. I troubleshoot hardware, Windows and application issues, help users understand solutions and test fixes. I would bring practical support experience, an analytical approach and clear communication to Smith+Nephew while developing ServiceNow and structured service desk practices.',skills=[
'First-line user support: clarifying issues, troubleshooting common faults, reproducing errors and checking proposed solutions.',
'Windows and Microsoft 365: strong application familiarity, workstation setup and support for everyday user problems.',
'Hardware and connectivity: PC troubleshooting, LAN cabling, switches and network devices; basic DHCP and routing concepts.',
'Documentation and testing: describing application behaviour, validating data and checking changes against user needs.',
'Basic Linux administration and diagnostics; Active Directory experience limited to joining computers to a domain.'],project='LabFlow | healthcare-related application project',projecttext='Demonstration laboratory workflow application built with Django and React. Designed process stages, forms, user roles and an audit trail; worked with PostgreSQL/SQLite, validation and testing. Prepared user and technical documentation, including setup and recovery guidance.')
}
for key,cfg in configs.items():
 en=cfg['en']
 b=[('name','Denis Gruszkiewicz'),('role',cfg['role']),('contact','Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com'),('contact','github.com/Flyingzaptop | antillia.tech'),('section','PROFILE' if en else 'PROFIL ZAWODOWY'),('body',cfg['profile']),('section','RELEVANT SKILLS' if en else 'KLUCZOWE KOMPETENCJE')]
 b += [('bullet',s) for s in cfg['skills']]
 b += [('section','PROFESSIONAL EXPERIENCE' if en else 'DOŚWIADCZENIE ZAWODOWE'),('title','Junior IT Administrator | ZOZ w Bolesławcu | 06.2025 - present' if en else 'Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie')]
 work_en=['Provide day-to-day technical support to hospital staff and diagnose hardware, operating system and application issues.','Configure workstations and network devices, connect switches and LAN cabling, and investigate connectivity problems.','Analyse user needs, reproduce reported errors and test application scenarios and fixes.','Develop internal tools for repetitive tasks; worked on separate employee-management, scheduling and laboratory-process applications.']
 work_pl=['Bieżące wsparcie techniczne pracowników szpitala oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych.','Konfiguracja stanowisk i urządzeń sieciowych, podłączanie switchy, okablowanie LAN i diagnostyka połączeń.','Analiza potrzeb użytkowników, odtwarzanie zgłaszanych błędów oraz testowanie scenariuszy działania i poprawek.','Rozwój narzędzi usprawniających powtarzalne czynności; praca nad oddzielnymi aplikacjami do zarządzania pracownikami, grafikiem i procesami laboratoryjnymi.']
 b += [('bullet',s) for s in (work_en if en else work_pl)]
 b += [('section','SELECTED PROJECTS' if en else 'WYBRANE PROJEKTY'),('title',cfg['project']),('body',cfg['projecttext'])]
 if key=='FOTC_EN': extra='LabFlow: Django/React laboratory workflow demo with user roles, validation and audit history; Windows/Ubuntu setup and recovery documentation.'
 elif en: extra='JobHunter: n8n/PostgreSQL workflow automation with automated tests and GitHub Actions CI. Additional engineering projects: Fusion 360, AutoCAD and RobotStudio.'
 else: extra='JobHunter: automatyzacja workflow n8n/PostgreSQL, testy i GitHub Actions CI. Dodatkowe projekty inżynierskie: Fusion 360, AutoCAD i RobotStudio.'
 b += [('body',extra),('section','EDUCATION' if en else 'WYKSZTAŁCENIE'),('title','WSB Merito we Wrocławiu | 03.2026 - present' if en else 'WSB Merito we Wrocławiu | 03.2026 - obecnie'),('body','Network, systems and IT security engineering; part-time engineering studies, second semester.' if en else 'Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr.'),('title','Politechnika Wrocławska | 10.2022 - present' if en else 'Politechnika Wrocławska | 10.2022 - obecnie'),('body','Robotics and Process Automation; engineering studies in progress, five semesters completed.' if en else 'Robotyka i Automatyzacja Procesów; studia inżynierskie w toku, ukończony V semestr.'),('section','LANGUAGES AND AVAILABILITY' if en else 'JĘZYKI I DOSTĘPNOŚĆ'),('body','Polish - advanced; English - advanced / technical; Ukrainian and Russian - native. IT Step Python AI course, 02.2024 - 12.2024. Category B driving licence.' if en else 'Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. IT Step: Python AI, 02.2024 - 12.2024. Prawo jazdy kat. B.'),('body','Seeking flexible working hours. From March 2027: available onsite in Wrocław up to 1-2 days per week, with remaining work remote. Open to part-time arrangements; start date by agreement.' if en else 'Poszukuję elastycznych godzin pracy. Od marca 2027: praca stacjonarna we Wrocławiu maksymalnie 1-2 dni w tygodniu, w pozostałe dni zdalnie. Możliwa część etatu; termin rozpoczęcia do uzgodnienia.')]
 story=[]
 for k,t in b:
  p=Paragraph(escape(('- ' if k=='bullet' else '')+t),styles[k]);p.keepWithNext=k in ['title','section'];story.append(p)
 path=out/f'Denis_Gruszkiewicz_CV_{key}.pdf'
 SimpleDocTemplate(str(path),pagesize=A4,leftMargin=40,rightMargin=40,topMargin=27,bottomMargin=28,title=f'Denis Gruszkiewicz - {key}',author='Denis Gruszkiewicz').build(story)
 (out/f'{key}_content.json').write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8')
 with pdfplumber.open(path) as doc:
  text=' '.join(p.extract_text() or '' for p in doc.pages)
  assert 'r3dflzp.ns@gmail.com' in text and '2027' in text
  assert len(doc.pages)==1,(key,len(doc.pages))
  print(key,len(doc.pages),'page; contact and availability verified')
 doc=pdfium.PdfDocument(str(path))
 for i,p in enumerate(doc):p.render(scale=1.5).to_pil().save(root/f'tmp/pdfs/{key}-{i+1}.png')



======== FILE: AmRest_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "IT Menu Junior Administrator | wsparcie aplikacji i testowanie zmian"
  ],
  [
    "contact",
    "Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "Portfolio projektowe: github.com/Flyingzaptop"
  ],
  [
    "section",
    "PROFIL ZAWODOWY"
  ],
  [
    "body",
    "Młodszy Administrator IT z ponad rokiem doświadczenia we wsparciu użytkowników i rozwiązywaniu problemów aplikacyjnych w szpitalu. Testuję scenariusze działania, odtwarzam błędy i rozwijam narzędzia usprawniające codzienną pracę. Bardzo dobrze znam Microsoft 365, pracuję z Windows i podstawami Linuxa oraz mam podstawy SQL i praktykę projektową z bazami danych. Chcę wykorzystać to zaplecze w IT Menu Management w AmRest: przy testowaniu zmian, wsparciu systemów i automatyzacji procesów."
  ],
  [
    "section",
    "KLUCZOWE KOMPETENCJE"
  ],
  [
    "bullet",
    "Wsparcie aplikacji i użytkowników: rozpoznawanie problemów, diagnoza, odtwarzanie błędów i wyjaśnianie sposobu działania systemów."
  ],
  [
    "bullet",
    "Testowanie zmian: sprawdzanie scenariuszy, walidacja danych, kontrola reguł procesu i weryfikacja poprawek."
  ],
  [
    "bullet",
    "Microsoft 365 / MS Office - bardzo dobra znajomość; Windows i podstawy Linuxa."
  ],
  [
    "bullet",
    "Podstawy SQL; projektowa praca z PostgreSQL i SQLite, strukturą danych oraz logiką aplikacji."
  ],
  [
    "bullet",
    "Automatyzacja i aplikacje webowe: Python, Django, React/TypeScript, n8n; dokumentacja techniczna i analiza potrzeb użytkowników."
  ],
  [
    "section",
    "DOŚWIADCZENIE ZAWODOWE"
  ],
  [
    "title",
    "Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie"
  ],
  [
    "bullet",
    "Bieżące wsparcie pracowników w obsłudze systemów oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych."
  ],
  [
    "bullet",
    "Testowanie scenariuszy działania i logiki aplikacji, odtwarzanie zgłaszanych błędów oraz sprawdzanie poprawności danych."
  ],
  [
    "bullet",
    "Analiza potrzeb użytkowników i rozwój wewnętrznych narzędzi upraszczających powtarzalne czynności."
  ],
  [
    "bullet",
    "Praca nad oddzielnymi rozwiązaniami do zarządzania pracownikami, grafikiem oraz procesami laboratoryjnymi."
  ],
  [
    "bullet",
    "Konfiguracja stanowisk i urządzeń sieciowych, podstawowa diagnostyka połączeń oraz dołączanie komputerów do domeny."
  ],
  [
    "section",
    "WYBRANE PROJEKTY"
  ],
  [
    "title",
    "LabFlow | aplikacja procesowa Django / React"
  ],
  [
    "body",
    "Demonstracyjny system koordynacji pracy laboratorium: etapy, statusy, formularze, role użytkowników i historia operacji. PostgreSQL/SQLite, testy reguł aplikacji oraz dokumentacja użytkownika i techniczna. Praktyka przekładania procesu użytkownika na czytelne zasady działania systemu."
  ],
  [
    "title",
    "JobHunter | automatyzacja workflow"
  ],
  [
    "body",
    "n8n, Node.js, PostgreSQL i Playwright; porządkowanie danych, walidacja schematów, panel React oraz testy i GitHub Actions CI. Projekt rozwijany lokalnie."
  ],
  [
    "section",
    "WYKSZTAŁCENIE"
  ],
  [
    "title",
    "WSB Merito we Wrocławiu | 03.2026 - obecnie"
  ],
  [
    "body",
    "Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr."
  ],
  [
    "title",
    "Politechnika Wrocławska | 10.2022 - obecnie"
  ],
  [
    "body",
    "Robotyka i Automatyzacja Procesów, studia inżynierskie; ukończony V semestr."
  ],
  [
    "section",
    "JĘZYKI I INFORMACJE DODATKOWE"
  ],
  [
    "body",
    "Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. IT Step: kurs Python AI, 02.2024 - 12.2024."
  ],
  [
    "body",
    "Dodatkowa praktyka: analiza danych w Pythonie oraz projekty Fusion 360, AutoCAD i RobotStudio. Prawo jazdy kat. B. Zainteresowanie pełnym etatem w modelu hybrydowym; termin rozpoczęcia do uzgodnienia."
  ]
]


======== FILE: BPX_PL_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "Młodszy Specjalista IT | Windows, Linux i wsparcie użytkowników"
  ],
  [
    "contact",
    "Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "github.com/Flyingzaptop | antillia.tech"
  ],
  [
    "section",
    "PROFIL ZAWODOWY"
  ],
  [
    "body",
    "Młodszy Administrator IT z ponad rokiem doświadczenia w szpitalu. Wspieram użytkowników, konfiguruję stanowiska i diagnozuję problemy sprzętowe, aplikacyjne oraz sieciowe. Znam Windows, Microsoft 365 i podstawy Linuxa; rozwijam również aplikacje i automatyzacje. Chcę wykorzystać te umiejętności w BPX przy przygotowywaniu środowisk i wsparciu klientów oraz rozwijać administrację infrastrukturą pod okiem mentora."
  ],
  [
    "section",
    "KLUCZOWE KOMPETENCJE"
  ],
  [
    "bullet",
    "Windows: konfiguracja stanowisk, instalacja aplikacji, diagnozowanie problemów oraz składanie, modernizacja i serwis komputerów."
  ],
  [
    "bullet",
    "Linux - podstawowa administracja i diagnostyka; projektowa dokumentacja uruchamiania aplikacji w Ubuntu."
  ],
  [
    "bullet",
    "Sieci: okablowanie LAN, podłączanie switchy i urządzeń, podstawy DHCP i routingu, diagnostyka połączeń."
  ],
  [
    "bullet",
    "Microsoft 365 - bardzo dobra znajomość pakietu. Active Directory - dołączanie komputerów do domeny."
  ],
  [
    "bullet",
    "Podstawy SQL, PostgreSQL/SQLite w projektach; Python, Git/GitHub, automatyzacja i testowanie aplikacji."
  ],
  [
    "section",
    "DOŚWIADCZENIE ZAWODOWE"
  ],
  [
    "title",
    "Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie"
  ],
  [
    "bullet",
    "Bieżące wsparcie techniczne pracowników szpitala oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych."
  ],
  [
    "bullet",
    "Konfiguracja stanowisk i urządzeń sieciowych, podłączanie switchy, okablowanie LAN i diagnostyka połączeń."
  ],
  [
    "bullet",
    "Analiza potrzeb użytkowników, odtwarzanie zgłaszanych błędów oraz testowanie scenariuszy działania i poprawek."
  ],
  [
    "bullet",
    "Rozwój narzędzi usprawniających powtarzalne czynności; praca nad oddzielnymi aplikacjami do zarządzania pracownikami, grafikiem i procesami laboratoryjnymi."
  ],
  [
    "section",
    "WYBRANE PROJEKTY"
  ],
  [
    "title",
    "LabFlow | konfiguracja i testowanie aplikacji"
  ],
  [
    "body",
    "Demonstracyjna aplikacja Django/React do koordynacji pracy laboratorium. Role użytkowników, walidacja danych i historia operacji; PostgreSQL/SQLite. Dokumentacja konfiguracji Windows/Ubuntu, backupu i odtwarzania oraz testowanie logiki procesu."
  ],
  [
    "body",
    "JobHunter: automatyzacja workflow n8n/PostgreSQL, testy i GitHub Actions CI. Dodatkowe projekty inżynierskie: Fusion 360, AutoCAD i RobotStudio."
  ],
  [
    "section",
    "WYKSZTAŁCENIE"
  ],
  [
    "title",
    "WSB Merito we Wrocławiu | 03.2026 - obecnie"
  ],
  [
    "body",
    "Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr."
  ],
  [
    "title",
    "Politechnika Wrocławska | 10.2022 - obecnie"
  ],
  [
    "body",
    "Robotyka i Automatyzacja Procesów; studia inżynierskie w toku, ukończony V semestr."
  ],
  [
    "section",
    "JĘZYKI I DOSTĘPNOŚĆ"
  ],
  [
    "body",
    "Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. IT Step: Python AI, 02.2024 - 12.2024. Prawo jazdy kat. B."
  ],
  [
    "body",
    "Poszukuję elastycznych godzin pracy. Od marca 2027: praca stacjonarna we Wrocławiu maksymalnie 1-2 dni w tygodniu, w pozostałe dni zdalnie. Możliwa część etatu; termin rozpoczęcia do uzgodnienia."
  ]
]


======== FILE: CUI_PL_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "Administrator IT | wsparcie aplikacji i systemów dziedzinowych"
  ],
  [
    "contact",
    "Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "github.com/Flyingzaptop | antillia.tech"
  ],
  [
    "section",
    "PROFIL ZAWODOWY"
  ],
  [
    "body",
    "Młodszy Administrator IT z ponad rokiem doświadczenia we wsparciu pracowników szpitala. Diagnozuję problemy aplikacyjne, systemowe i sprzętowe, odtwarzam błędy oraz testuję poprawki. Łączę kontakt z użytkownikami z projektową pracą nad aplikacjami Django/React i bazami danych. Chcę wykorzystać to zaplecze w CUI przy utrzymaniu aplikacji biznesowych, obsłudze zgłoszeń i rozwoju dokumentacji."
  ],
  [
    "section",
    "KLUCZOWE KOMPETENCJE"
  ],
  [
    "bullet",
    "Wsparcie aplikacji: diagnozowanie problemów, odtwarzanie błędów, testowanie scenariuszy i weryfikacja poprawności danych."
  ],
  [
    "bullet",
    "Podstawy SQL; praktyka projektowa z PostgreSQL i SQLite oraz strukturą danych w aplikacjach."
  ],
  [
    "bullet",
    "Role i uprawnienia użytkowników, historia operacji i walidacja danych w projekcie LabFlow."
  ],
  [
    "bullet",
    "Windows, Microsoft 365 - bardzo dobra znajomość pakietu i wsparcie użytkowników; podstawy administracji i diagnostyki Linux."
  ],
  [
    "bullet",
    "Dokumentowanie konfiguracji i działania aplikacji; analiza potrzeb użytkowników, Python i automatyzacja powtarzalnych czynności."
  ],
  [
    "section",
    "DOŚWIADCZENIE ZAWODOWE"
  ],
  [
    "title",
    "Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie"
  ],
  [
    "bullet",
    "Bieżące wsparcie techniczne pracowników szpitala oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych."
  ],
  [
    "bullet",
    "Konfiguracja stanowisk i urządzeń sieciowych, podłączanie switchy, okablowanie LAN i diagnostyka połączeń."
  ],
  [
    "bullet",
    "Analiza potrzeb użytkowników, odtwarzanie zgłaszanych błędów oraz testowanie scenariuszy działania i poprawek."
  ],
  [
    "bullet",
    "Rozwój narzędzi usprawniających powtarzalne czynności; praca nad oddzielnymi aplikacjami do zarządzania pracownikami, grafikiem i procesami laboratoryjnymi."
  ],
  [
    "section",
    "WYBRANE PROJEKTY"
  ],
  [
    "title",
    "LabFlow | aplikacja procesowa Django / React"
  ],
  [
    "body",
    "Demonstracyjny system koordynacji procesów laboratoryjnych: etapy, statusy, formularze, role użytkowników i historia operacji. PostgreSQL/SQLite, testowanie reguł aplikacji oraz dokumentacja konfiguracji Windows/Ubuntu, backupu i odtwarzania. Projekt pokazuje umiejętność przekładania potrzeb użytkowników na działający system."
  ],
  [
    "body",
    "JobHunter: automatyzacja workflow n8n/PostgreSQL, testy i GitHub Actions CI. Dodatkowe projekty inżynierskie: Fusion 360, AutoCAD i RobotStudio."
  ],
  [
    "section",
    "WYKSZTAŁCENIE"
  ],
  [
    "title",
    "WSB Merito we Wrocławiu | 03.2026 - obecnie"
  ],
  [
    "body",
    "Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr."
  ],
  [
    "title",
    "Politechnika Wrocławska | 10.2022 - obecnie"
  ],
  [
    "body",
    "Robotyka i Automatyzacja Procesów; studia inżynierskie w toku, ukończony V semestr."
  ],
  [
    "section",
    "JĘZYKI I DOSTĘPNOŚĆ"
  ],
  [
    "body",
    "Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. IT Step: Python AI, 02.2024 - 12.2024. Prawo jazdy kat. B."
  ],
  [
    "body",
    "Poszukuję elastycznych godzin pracy. Od marca 2027: praca stacjonarna we Wrocławiu maksymalnie 1-2 dni w tygodniu, w pozostałe dni zdalnie. Możliwa część etatu; termin rozpoczęcia do uzgodnienia."
  ]
]


======== FILE: DCG_Security_PL_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "Młodszy Specjalista Bezpieczeństwa IT | wsparcie IT i diagnostyka"
  ],
  [
    "contact",
    "Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "Portfolio techniczne: github.com/Flyingzaptop"
  ],
  [
    "section",
    "PROFIL ZAWODOWY"
  ],
  [
    "body",
    "Młodszy Administrator IT z ponad rokiem doświadczenia we wsparciu pracowników szpitala. Diagnozuję problemy sprzętowe, systemowe i aplikacyjne, odtwarzam błędy oraz weryfikuję poprawki. Studiuję inżynierię sieci, systemów i bezpieczeństwa IT. Chcę wykorzystać doświadczenie w obsłudze problemów użytkowników i analizie danych w zespole bezpieczeństwa DCG, rozwijając kompetencje w analizie alertów SIEM, EDR/XDR i DLP."
  ],
  [
    "section",
    "KOMPETENCJE PRZYDATNE W OPERACJACH BEZPIECZEŃSTWA"
  ],
  [
    "bullet",
    "Diagnostyka: zbieranie informacji o problemie, odtwarzanie błędów, weryfikacja działania aplikacji i poprawności danych."
  ],
  [
    "bullet",
    "Windows i sprzęt PC: konfiguracja stanowisk, rozwiązywanie problemów systemowych, modernizacja i serwis komputerów."
  ],
  [
    "bullet",
    "Sieci: okablowanie LAN, podłączanie switchy i urządzeń, podstawy DHCP i routingu oraz diagnostyka połączeń."
  ],
  [
    "bullet",
    "Linux - podstawowa administracja i diagnostyka. Active Directory - dołączanie komputerów do domeny. Microsoft 365 - bardzo dobra znajomość pakietu."
  ],
  [
    "bullet",
    "Python, podstawy SQL, PostgreSQL/SQLite; Git/GitHub, testowanie aplikacji i automatyzacja workflow w projektach własnych."
  ],
  [
    "section",
    "DOŚWIADCZENIE ZAWODOWE"
  ],
  [
    "title",
    "Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie"
  ],
  [
    "bullet",
    "Bieżące wsparcie techniczne pracowników oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych."
  ],
  [
    "bullet",
    "Konfiguracja stanowisk i urządzeń sieciowych, okablowanie LAN oraz podstawowa diagnostyka połączeń."
  ],
  [
    "bullet",
    "Analiza potrzeb użytkowników, odtwarzanie zgłaszanych błędów, testowanie scenariuszy i sprawdzanie poprawności danych."
  ],
  [
    "bullet",
    "Rozwój wewnętrznych narzędzi usprawniających powtarzalne czynności; oddzielne aplikacje dla pracowników, grafików i procesów laboratoryjnych."
  ],
  [
    "section",
    "PROJEKTY TECHNICZNE"
  ],
  [
    "title",
    "LabFlow | role użytkowników, walidacja i historia operacji"
  ],
  [
    "body",
    "Demonstracyjny system Django/React do koordynacji procesów laboratoryjnych. Role i uprawnienia użytkowników, audyt operacji, PostgreSQL/SQLite oraz testowanie reguł aplikacji. Dokumentacja konfiguracji Windows/Ubuntu, backupu i odtwarzania."
  ],
  [
    "title",
    "JobHunter | automatyzacja i kontrola jakości danych"
  ],
  [
    "body",
    "n8n, PostgreSQL, lokalna LLM, Playwright i panel React. Deterministyczne przetwarzanie danych, walidacja wyników, testy oraz GitHub Actions CI. Praktyka analizowania problemów na styku kilku usług."
  ],
  [
    "body",
    "Dodatkowe zaplecze inżynierskie: Fusion 360, AutoCAD i RobotStudio; projekt przekładni cykloidalnej."
  ],
  [
    "section",
    "WYKSZTAŁCENIE"
  ],
  [
    "title",
    "WSB Merito we Wrocławiu | 03.2026 - obecnie"
  ],
  [
    "body",
    "Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr."
  ],
  [
    "title",
    "Politechnika Wrocławska | 10.2022 - obecnie"
  ],
  [
    "body",
    "Robotyka i Automatyzacja Procesów; studia inżynierskie w toku, ukończony V semestr."
  ],
  [
    "section",
    "JĘZYKI I DOSTĘPNOŚĆ"
  ],
  [
    "body",
    "Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. Prawo jazdy kat. B. IT Step: Python AI, 02.2024 - 12.2024."
  ],
  [
    "body",
    "Elastyczne godziny pracy; możliwa część etatu. Od marca 2027 maksymalnie 1-2 dni w tygodniu stacjonarnie we Wrocławiu, pozostała praca zdalnie. Termin rozpoczęcia do uzgodnienia."
  ]
]


======== FILE: DRACO_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "Młodszy Specjalista ds. Wsparcia IT i Administracji Systemami"
  ],
  [
    "contact",
    "Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "Prawo jazdy kat. B od 3 lat | Gotowość do wizyt i dyżurów u klientów"
  ],
  [
    "section",
    "PROFIL ZAWODOWY"
  ],
  [
    "body",
    "Młodszy Administrator IT z ponad rokiem doświadczenia w szpitalu. Wspieram użytkowników, diagnozuję problemy sprzętowe, systemowe i aplikacyjne oraz konfiguruję stanowiska i urządzenia sieciowe. Bardzo dobrze znam Microsoft 365, mam praktykę w dołączaniu komputerów do domeny i podstawy pracy z Linuxem. Chcę wykorzystać to doświadczenie w DRACO i rozwijać administrację systemami przy wsparciu bardziej doświadczonego administratora."
  ],
  [
    "section",
    "KLUCZOWE KOMPETENCJE"
  ],
  [
    "bullet",
    "Windows i sprzęt PC: diagnozowanie problemów, konfiguracja stanowisk, składanie, modernizacja i serwis komputerów."
  ],
  [
    "bullet",
    "Microsoft 365 - bardzo dobra znajomość pakietu; wsparcie użytkowników w codziennej pracy z aplikacjami."
  ],
  [
    "bullet",
    "Active Directory - podstawowy zakres praktyczny: dołączanie komputerów do domeny."
  ],
  [
    "bullet",
    "Sieci: okablowanie LAN, podłączanie switchy i urządzeń, podstawy DHCP i routingu oraz diagnostyka połączeń."
  ],
  [
    "bullet",
    "Linux - podstawowa administracja i diagnostyka; testowanie działania aplikacji, odtwarzanie błędów i walidacja danych."
  ],
  [
    "section",
    "DOŚWIADCZENIE ZAWODOWE"
  ],
  [
    "title",
    "Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie"
  ],
  [
    "bullet",
    "Bieżące wsparcie techniczne pracowników: rozpoznawanie problemów sprzętowych, systemowych i aplikacyjnych oraz pomoc w ich rozwiązaniu."
  ],
  [
    "bullet",
    "Podłączanie i konfiguracja stanowisk, switchy i urządzeń sieciowych; prowadzenie okablowania LAN i podstawowa diagnostyka połączeń."
  ],
  [
    "bullet",
    "Analiza potrzeb użytkowników i rozwój wewnętrznych narzędzi upraszczających powtarzalne czynności."
  ],
  [
    "bullet",
    "Testowanie scenariuszy, odtwarzanie zgłaszanych błędów i poprawianie aplikacji na podstawie potrzeb pracowników."
  ],
  [
    "section",
    "PROJEKTY I AUTOMATYZACJA"
  ],
  [
    "body",
    "LabFlow: demonstracyjna aplikacja Django/React do koordynacji procesów laboratoryjnych, z rolami użytkowników i audytem; dokumentacja konfiguracji Windows/Ubuntu oraz backupu i odtwarzania. JobHunter: automatyzacja workflow z n8n, PostgreSQL i lokalną LLM; GitHub Actions CI. Python i narzędzia AI wykorzystuję do analizy kodu i prototypowania."
  ],
  [
    "contact",
    "Portfolio techniczne: github.com/Flyingzaptop"
  ],
  [
    "section",
    "WYKSZTAŁCENIE"
  ],
  [
    "title",
    "WSB Merito we Wrocławiu | 03.2026 - obecnie"
  ],
  [
    "body",
    "Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr."
  ],
  [
    "title",
    "Politechnika Wrocławska | 10.2022 - obecnie"
  ],
  [
    "body",
    "Robotyka i Automatyzacja Procesów, studia inżynierskie; ukończony V semestr."
  ],
  [
    "section",
    "JĘZYKI I INFORMACJE DODATKOWE"
  ],
  [
    "body",
    "Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. Kurs IT Step Python AI: 02.2024 - 12.2024."
  ],
  [
    "body",
    "Dodatkowe zaplecze: Fusion 360, AutoCAD, RobotStudio i własne projekty mechaniczne. Zainteresowanie pracą na część etatu lub pełny etat w modelu hybrydowym; termin rozpoczęcia do uzgodnienia."
  ]
]


======== FILE: FOTC_EN_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "Junior Cloud Support | IT troubleshooting and workflow automation"
  ],
  [
    "contact",
    "Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "github.com/Flyingzaptop | antillia.tech"
  ],
  [
    "section",
    "PROFILE"
  ],
  [
    "body",
    "Junior IT Administrator with over a year of hands-on experience supporting hospital staff, troubleshooting Windows, hardware and application issues, and configuring workstations. I combine user support with basic Linux and networking knowledge and practical web application projects. I want to bring this troubleshooting approach to FOTC and develop expertise in Google Workspace and SaaS support."
  ],
  [
    "section",
    "RELEVANT SKILLS"
  ],
  [
    "bullet",
    "User support: understanding reported issues, reproducing errors, explaining solutions and checking that fixes work."
  ],
  [
    "bullet",
    "Windows and Microsoft 365: strong application familiarity and day-to-day user support; workstation setup and PC troubleshooting."
  ],
  [
    "bullet",
    "Networking: LAN cabling, connecting switches and devices, basic DHCP and routing concepts, connectivity troubleshooting."
  ],
  [
    "bullet",
    "Linux: basic administration and diagnostics. Active Directory: practical experience joining computers to a domain."
  ],
  [
    "bullet",
    "Automation and data: Python, n8n, PostgreSQL/SQLite, basic SQL; Git/GitHub and automated testing in personal projects."
  ],
  [
    "section",
    "PROFESSIONAL EXPERIENCE"
  ],
  [
    "title",
    "Junior IT Administrator | ZOZ w Bolesławcu | 06.2025 - present"
  ],
  [
    "bullet",
    "Provide day-to-day technical support to hospital staff and diagnose hardware, operating system and application issues."
  ],
  [
    "bullet",
    "Configure workstations and network devices, connect switches and LAN cabling, and investigate connectivity problems."
  ],
  [
    "bullet",
    "Analyse user needs, reproduce reported errors and test application scenarios and fixes."
  ],
  [
    "bullet",
    "Develop internal tools for repetitive tasks; worked on separate employee-management, scheduling and laboratory-process applications."
  ],
  [
    "section",
    "SELECTED PROJECTS"
  ],
  [
    "title",
    "JobHunter - workflow automation"
  ],
  [
    "body",
    "Personal automation platform combining n8n, PostgreSQL, local LLM services, Playwright and a React dashboard. Worked with structured data, workflow validation, automated tests and GitHub Actions CI. This supports a systematic approach to investigating problems across connected services."
  ],
  [
    "body",
    "LabFlow: Django/React laboratory workflow demo with user roles, validation and audit history; Windows/Ubuntu setup and recovery documentation."
  ],
  [
    "section",
    "EDUCATION"
  ],
  [
    "title",
    "WSB Merito we Wrocławiu | 03.2026 - present"
  ],
  [
    "body",
    "Network, systems and IT security engineering; part-time engineering studies, second semester."
  ],
  [
    "title",
    "Politechnika Wrocławska | 10.2022 - present"
  ],
  [
    "body",
    "Robotics and Process Automation; engineering studies in progress, five semesters completed."
  ],
  [
    "section",
    "LANGUAGES AND AVAILABILITY"
  ],
  [
    "body",
    "Polish - advanced; English - advanced / technical; Ukrainian and Russian - native. IT Step Python AI course, 02.2024 - 12.2024. Category B driving licence."
  ],
  [
    "body",
    "Seeking flexible working hours. From March 2027: available onsite in Wrocław up to 1-2 days per week, with remaining work remote. Open to part-time arrangements; start date by agreement."
  ]
]


======== FILE: Greenbrier_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "Młodszy Konstruktor | CAD 2D/3D, mechanika i prototypowanie"
  ],
  [
    "contact",
    "Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "Prawo jazdy kat. B od 3 lat | github.com/Flyingzaptop - projekty IT i R&D"
  ],
  [
    "section",
    "PROFIL ZAWODOWY"
  ],
  [
    "body",
    "Student Robotyki i Automatyzacji Procesów na Politechnice Wrocławskiej, po ukończeniu V semestru. Rozwijam własne projekty mechaniczne i akademickie projekty robotyki, łącząc modelowanie 3D, rysunek techniczny i analizę współpracy elementów. Pracuję przede wszystkim w Fusion 360 i AutoCAD. Chcę wykorzystać tę podstawę na stanowisku Młodszego Konstruktora w Greenbrier, rozwijając umiejętność przygotowywania modeli, rysunków i dokumentacji oraz poznając normy branży kolejowej. Dodatkowym atutem jest doświadczenie zawodowe w diagnozowaniu problemów technicznych i testowaniu aplikacji."
  ],
  [
    "section",
    "KOMPETENCJE KONSTRUKCYJNE"
  ],
  [
    "bullet",
    "Fusion 360 - główne środowisko modelowania 3D; części, złożenia i analiza geometrii konstrukcji."
  ],
  [
    "bullet",
    "AutoCAD - rysunek 2D i dokumentacja techniczna; interpretacja rysunków oraz przestrzenne rozumienie konstrukcji."
  ],
  [
    "bullet",
    "Projektowanie mechanizmów: analiza zasady działania, współpracy elementów, montażu, tolerancji i precyzji wykonania w projektach własnych."
  ],
  [
    "bullet",
    "Prototypowanie: modele STEP/STL, przygotowanie elementów do druku 3D i uwzględnianie ograniczeń technologii FDM."
  ],
  [
    "bullet",
    "Siemens NX i FluidSim - podstawy; RobotStudio - akademickie stanowiska spawania i paletyzacji."
  ],
  [
    "bullet",
    "Podstawy projektowania maszyn, mechaniki, technologii materiałów i procesów obróbki rozwijane w ramach studiów."
  ],
  [
    "section",
    "WYBRANE PROJEKTY INŻYNIERSKIE"
  ],
  [
    "title",
    "Przekładnia cykloidalna | projekt własny"
  ],
  [
    "bullet",
    "Projektowanie geometrii przekładni oraz modelowanie części mechanicznych."
  ],
  [
    "bullet",
    "Analiza zasady działania i współpracy elementów mechanizmu, z uwzględnieniem montażu, tolerancji oraz praktycznego wykonania."
  ],
  [
    "title",
    "Osiowy silnik odrzutowy | projekt koncepcyjny"
  ],
  [
    "bullet",
    "Samodzielne opracowanie koncepcji oraz modelowanie głównych elementów konstrukcyjnych w CAD."
  ],
  [
    "bullet",
    "Analiza geometrii, układu przepływu i rozmieszczenia komponentów; wizualizacja rozwiązania technicznego."
  ],
  [
    "title",
    "RobotStudio | projekty akademickie"
  ],
  [
    "bullet",
    "Projektowanie stanowisk zrobotyzowanych dla procesów spawania i paletyzacji."
  ],
  [
    "bullet",
    "Analiza trajektorii, zasięgu robota, organizacji stanowiska i logiki kolejnych etapów procesu."
  ],
  [
    "title",
    "Druk 3D i prototypowanie | projekty własne"
  ],
  [
    "body",
    "Projektowanie elementów pod druk 3D i praca z modelami STEP/STL. Uwzględnianie ograniczeń FDM oraz praktyczne podejście do montażu, testowania i poprawiania konstrukcji."
  ],
  [
    "page",
    ""
  ],
  [
    "section",
    "WYKSZTAŁCENIE"
  ],
  [
    "title",
    "Politechnika Wrocławska | 10.2022 - obecnie"
  ],
  [
    "body",
    "Robotyka i Automatyzacja Procesów, studia inżynierskie w toku; ukończony V semestr."
  ],
  [
    "bullet",
    "Zakres: mechanika, fizyka techniczna, matematyka inżynierska, rysunek techniczny, CAD, projektowanie maszyn, automatyka i robotyka przemysłowa."
  ],
  [
    "bullet",
    "Projekty i zajęcia związane ze stanowiskami zrobotyzowanymi, spawaniem, paletyzacją, obróbką materiałów i symulacją układów."
  ],
  [
    "title",
    "Uniwersytet WSB Merito we Wrocławiu | 03.2026 - obecnie"
  ],
  [
    "body",
    "Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr. Rozwijanie kompetencji informatycznych wspierających analizę danych i pracę z systemami technicznymi."
  ],
  [
    "section",
    "DOŚWIADCZENIE ZAWODOWE"
  ],
  [
    "title",
    "Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie"
  ],
  [
    "bullet",
    "Bieżące wsparcie techniczne pracowników oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych."
  ],
  [
    "bullet",
    "Analiza potrzeb użytkowników, odtwarzanie błędów i testowanie scenariuszy działania narzędzi."
  ],
  [
    "bullet",
    "Rozwój wewnętrznych aplikacji usprawniających pracę: oddzielne projekty zarządzania pracownikami, grafikiem i procesami laboratoryjnymi."
  ],
  [
    "bullet",
    "Podłączanie i konfiguracja stanowisk oraz urządzeń sieciowych, okablowanie LAN i podstawowa diagnostyka połączeń."
  ],
  [
    "section",
    "DODATKOWE PROJEKTY I UMIEJĘTNOŚCI TECHNICZNE"
  ],
  [
    "title",
    "Analiza danych i programowanie"
  ],
  [
    "body",
    "Python, NumPy i Pandas; własne badania danych czasowych i modeli ML. Pozyskiwanie i przygotowanie danych, projektowanie metryk, porównywanie eksperymentów oraz analiza błędów i ograniczeń wyników."
  ],
  [
    "title",
    "LabFlow i ARC | projekty software / R&D"
  ],
  [
    "body",
    "LabFlow: demonstracyjna aplikacja Django/React odwzorowująca wieloetapowy proces laboratoryjny, z rolami, walidacją i audytem. ARC: eksperymentalny runtime C++/D3D12, analiza zasobów, zależności i wydajności oraz testy. Projekty rozwijają systemowe podejście do problemów i weryfikacji rozwiązań."
  ],
  [
    "body",
    "Bardzo dobra znajomość Microsoft 365 / MS Office, w tym Excel i PowerPoint. Diagnostyka, składanie i modernizacja komputerów PC, także konfiguracji hard-tube water cooling. Współtworzenie inicjatywy Antillia związanej z aplikacjami i automatyzacją."
  ],
  [
    "section",
    "KURSY, JĘZYKI I INFORMACJE DODATKOWE"
  ],
  [
    "body",
    "IT Step - Python AI | 02.2024 - 12.2024; kurs programowania w Pythonie i sztucznej inteligencji."
  ],
  [
    "body",
    "Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste."
  ],
  [
    "body",
    "Prawo jazdy kat. B od 3 lat. Miejsce zamieszkania: Wrocław. Termin rozpoczęcia pracy do uzgodnienia."
  ]
]


======== FILE: iClan3D_CAD_PL_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "Konstruktor CAD 3D / dokumentacja 2D | Fusion 360 i AutoCAD"
  ],
  [
    "contact",
    "Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "Projekty mechaniczne: przekładnia cykloidalna, prototypowanie FDM"
  ],
  [
    "section",
    "PROFIL ZAWODOWY"
  ],
  [
    "body",
    "Student Robotyki i Automatyzacji Procesów na Politechnice Wrocławskiej, po ukończeniu V semestru. Modeluję części i złożenia w Fusion 360, pracuję z AutoCAD oraz rozwijam dokumentację techniczną własnych projektów. Projekt przekładni cykloidalnej obejmuje rysunek złożeniowy, zestawienie części i rysunki elementów. Chcę wykorzystać to zaplecze w iClan3D przy modelowaniu 3D i przygotowywaniu dokumentacji 2D oraz rozwijać pracę w Inventor i Navisworks."
  ],
  [
    "section",
    "KOMPETENCJE CAD I DOKUMENTACJA"
  ],
  [
    "bullet",
    "Fusion 360 - modelowanie części i złożeń, analiza geometrii oraz współpracy elementów konstrukcji."
  ],
  [
    "bullet",
    "AutoCAD - rysunek 2D i dokumentacja techniczna; czytanie rysunków i przestrzenna interpretacja konstrukcji."
  ],
  [
    "bullet",
    "Rysunki części i złożenia: wymiary, przekroje, oznaczenia elementów i zestawienie części; wybrane pasowania, tolerancje i chropowatość w projekcie przekładni."
  ],
  [
    "bullet",
    "STEP/STL, przygotowanie modeli pod druk 3D; uwzględnianie ograniczeń FDM, montażu i praktycznego wykonania."
  ],
  [
    "bullet",
    "Podstawy mechaniki, konstrukcji maszyn, materiałów i procesów obróbki ze studiów. Siemens NX - podstawy; RobotStudio - projekty akademickie."
  ],
  [
    "section",
    "WYBRANE PROJEKTY INŻYNIERSKIE"
  ],
  [
    "title",
    "Cyclo - przekładnia cykloidalna | projekt własny"
  ],
  [
    "bullet",
    "Opracowanie geometrii i modelowanie części przekładni; analiza zasady działania, współpracy elementów i zagadnień montażu."
  ],
  [
    "bullet",
    "Dokumentacja obejmująca 7 arkuszy: złożenie oraz wał wejściowy, koło cykloidalne, korpus, mocowanie, tarczę wyjściową i sworzeń."
  ],
  [
    "bullet",
    "Przekroje, oznaczenia części i zestawienie elementów zespołu; wymiary oraz wybrane pasowania, tolerancje i oznaczenia chropowatości."
  ],
  [
    "title",
    "Osiowy silnik odrzutowy | projekt koncepcyjny"
  ],
  [
    "body",
    "Koncepcja i modele głównych elementów konstrukcyjnych; analiza geometrii, układu przepływu i rozmieszczenia komponentów."
  ],
  [
    "title",
    "RobotStudio i prototypowanie FDM"
  ],
  [
    "body",
    "Akademickie stanowiska spawania i paletyzacji: trajektorie, zasięg robota i organizacja procesu. Własne elementy pod druk 3D oraz praca z modelami STEP/STL."
  ],
  [
    "section",
    "DOŚWIADCZENIE I DODATKOWE UMIEJĘTNOŚCI"
  ],
  [
    "title",
    "Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie"
  ],
  [
    "body",
    "Wsparcie użytkowników, diagnozowanie usterek, testowanie aplikacji i rozwój wewnętrznych narzędzi. Praktyka samodzielnego rozwiązywania problemów technicznych i analizy potrzeb użytkowników."
  ],
  [
    "body",
    "Python, NumPy/Pandas, podstawy SQL; bardzo dobra znajomość Microsoft 365. LabFlow - aplikacja procesowa; JobHunter - automatyzacja workflow. Portfolio software: github.com/Flyingzaptop."
  ],
  [
    "section",
    "WYKSZTAŁCENIE"
  ],
  [
    "title",
    "Politechnika Wrocławska | 10.2022 - obecnie"
  ],
  [
    "body",
    "Robotyka i Automatyzacja Procesów; studia inżynierskie w toku, ukończony V semestr."
  ],
  [
    "title",
    "WSB Merito we Wrocławiu | 03.2026 - obecnie"
  ],
  [
    "body",
    "Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr."
  ],
  [
    "section",
    "JĘZYKI I DOSTĘPNOŚĆ"
  ],
  [
    "body",
    "Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste. Prawo jazdy kat. B. IT Step: Python AI, 02.2024 - 12.2024."
  ],
  [
    "body",
    "Elastyczne godziny pracy; możliwa część etatu. Od marca 2027 maksymalnie 1-2 dni w tygodniu stacjonarnie we Wrocławiu, pozostała praca zdalnie. Termin rozpoczęcia do uzgodnienia."
  ]
]


======== FILE: Opera_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "AI / ML Engineering | Python, neural networks and experimental research"
  ],
  [
    "contact",
    "Wrocław, Poland | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "GitHub: github.com/Flyingzaptop"
  ],
  [
    "section",
    "PROFILE"
  ],
  [
    "body",
    "Engineering student and Junior IT Administrator with multi-year independent research in financial time series and neural networks. I build data pipelines, design features and training targets, compare model architectures and investigate failure modes. My projects combine Python/PyTorch, causal validation and reproducible experiments with local LLM integrations and application development. I am interested in contributing this research and software foundation to Opera’s AI team in Wrocław."
  ],
  [
    "section",
    "CORE SKILLS"
  ],
  [
    "bullet",
    "Python, PyTorch, NumPy, Pandas, Polars and PyArrow/Parquet; Jupyter/Colab and Matplotlib for analysis and visualization."
  ],
  [
    "bullet",
    "Neural sequence modeling: TCN, LSTM and RetNet-lite; feature/label design, custom losses, checkpointing and evaluation."
  ],
  [
    "bullet",
    "Experimental methods: chronological validation, data-leakage checks, baseline comparisons, error analysis and interpretation of negative results."
  ],
  [
    "bullet",
    "LLM applications: local Ollama/LM Studio, OpenAI API integration and academic Hugging Face Transformers text-generation practice."
  ],
  [
    "bullet",
    "Software: Django REST Framework, REST APIs, PostgreSQL/SQLite, basic SQL, React/TypeScript; GitHub Actions, pytest and native Rust/PyO3 components."
  ],
  [
    "section",
    "SELECTED MACHINE LEARNING RESEARCH"
  ],
  [
    "title",
    "XAUUSD angular sequence research | independent project"
  ],
  [
    "bullet",
    "Implemented experimental PyTorch TCN models and an asynchronous event branch with learned attention pooling, custom losses and geometric output constraints."
  ],
  [
    "bullet",
    "Investigated chronological forecasting, distillation and reconstruction as separate tasks; used causality tests and controlled baseline comparisons."
  ],
  [
    "body",
    "github.com/Flyingzaptop/xauusd"
  ],
  [
    "title",
    "stargazin | sequence models and offline/online consistency"
  ],
  [
    "bullet",
    "Built a pipeline covering Parquet ingestion, normalization, features, labels, dataset assembly, training/checkpointing and offline scoring."
  ],
  [
    "bullet",
    "Explored CT-LSTM and RetNet-lite variants, three-class output heads and margin objectives; investigated unstable predictions and preprocessing consistency."
  ],
  [
    "bullet",
    "Used Rust/PyO3 extensions for selected preprocessing paths and maintained unit, integration and regression tests."
  ],
  [
    "body",
    "github.com/Flyingzaptop/stargazin"
  ],
  [
    "page",
    ""
  ],
  [
    "section",
    "DATA QUALITY AND EXPERIMENT VALIDATION"
  ],
  [
    "title",
    "GC MBO research | event-level market-data experiments"
  ],
  [
    "bullet",
    "Python feature engineering and model experiments on CME Gold MBO/L3 data; Rust replay and conservative FIFO execution simulation."
  ],
  [
    "bullet",
    "Evaluated hypotheses using walk-forward analysis, causality checks and execution-cost/latency stress. Documented failed hypotheses and limits rather than treating backtests as proof of a usable strategy."
  ],
  [
    "body",
    "github.com/Flyingzaptop/gc-mbo-research"
  ],
  [
    "body",
    "Additional practice: stargaze-l2-vwap - async collectors and recoverable Parquet storage; Python-Colab - scikit-learn preprocessing/regression, NLTK and TF-IDF/SVD/SVC text classification."
  ],
  [
    "section",
    "LLM APPLICATIONS AND SOFTWARE PROJECTS"
  ],
  [
    "title",
    "JobHunter | structured LLM analysis and workflow automation"
  ],
  [
    "body",
    "Node.js/n8n, PostgreSQL, Ollama and Playwright; deterministic processing, schema-validated LLM analysis, React/SSE dashboard and human-in-the-loop controls. Docker Compose configuration and GitHub Actions CI. Local project under development: github.com/Flyingzaptop/jobhunter-n8n."
  ],
  [
    "title",
    "LabFlow | process application and local AI integrations"
  ],
  [
    "body",
    "Django REST Framework + React/TypeScript, REST/OpenAPI, RBAC and audit logging. Implemented local Ollama streaming client and optional faster-whisper speech-to-text. Public demonstrator with fictional data: github.com/Flyingzaptop/LabFlow."
  ],
  [
    "body",
    "ARC: experimental C++/D3D12 resource and performance research with CMake/CTest CI. MultiNeuro: Python Telegram bot using OpenAI API. Antillia: co-developing an early-stage web/software/AI initiative (antillia.tech)."
  ],
  [
    "section",
    "PROFESSIONAL EXPERIENCE"
  ],
  [
    "title",
    "Junior IT Administrator | ZOZ w Bolesławcu | 06.2025 - present"
  ],
  [
    "bullet",
    "Support staff, diagnose hardware/system/application issues and develop internal tools based on user needs."
  ],
  [
    "bullet",
    "Test application scenarios, validate data, reproduce defects and improve application logic; separate projects for employee management, schedules and laboratory coordination."
  ],
  [
    "section",
    "EDUCATION AND TRAINING"
  ],
  [
    "title",
    "Wrocław University of Science and Technology | 10.2022 - present"
  ],
  [
    "body",
    "Robotics and Process Automation, engineering studies; completed the fifth semester. Coursework includes engineering mathematics, physics, mechanics, automation and robotics."
  ],
  [
    "title",
    "WSB Merito University in Wrocław | 03.2026 - present"
  ],
  [
    "body",
    "Network, Systems and IT Security Engineering; part-time studies, second semester."
  ],
  [
    "body",
    "IT Step - Python AI, 02.2024 - 12.2024; Python and AI grades: 10/10 each."
  ],
  [
    "section",
    "LANGUAGES AND ENGINEERING BACKGROUND"
  ],
  [
    "body",
    "Polish: advanced; English: advanced / technical; Ukrainian and Russian: native. CAD/robotics projects: Fusion 360, AutoCAD, RobotStudio, cycloidal drive, axial turbojet concept and 3D-printing components."
  ]
]


======== FILE: Smith_Nephew_EN_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "IT Service Desk Level 1 Intern | user support and troubleshooting"
  ],
  [
    "contact",
    "Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "github.com/Flyingzaptop | antillia.tech"
  ],
  [
    "section",
    "PROFILE"
  ],
  [
    "body",
    "Junior IT Administrator with over a year of experience supporting staff in a healthcare environment and a current part-time IT student. I troubleshoot hardware, Windows and application issues, help users understand solutions and test fixes. I would bring practical support experience, an analytical approach and clear communication to Smith+Nephew while developing ServiceNow and structured service desk practices."
  ],
  [
    "section",
    "RELEVANT SKILLS"
  ],
  [
    "bullet",
    "First-line user support: clarifying issues, troubleshooting common faults, reproducing errors and checking proposed solutions."
  ],
  [
    "bullet",
    "Windows and Microsoft 365: strong application familiarity, workstation setup and support for everyday user problems."
  ],
  [
    "bullet",
    "Hardware and connectivity: PC troubleshooting, LAN cabling, switches and network devices; basic DHCP and routing concepts."
  ],
  [
    "bullet",
    "Documentation and testing: describing application behaviour, validating data and checking changes against user needs."
  ],
  [
    "bullet",
    "Basic Linux administration and diagnostics; Active Directory experience limited to joining computers to a domain."
  ],
  [
    "section",
    "PROFESSIONAL EXPERIENCE"
  ],
  [
    "title",
    "Junior IT Administrator | ZOZ w Bolesławcu | 06.2025 - present"
  ],
  [
    "bullet",
    "Provide day-to-day technical support to hospital staff and diagnose hardware, operating system and application issues."
  ],
  [
    "bullet",
    "Configure workstations and network devices, connect switches and LAN cabling, and investigate connectivity problems."
  ],
  [
    "bullet",
    "Analyse user needs, reproduce reported errors and test application scenarios and fixes."
  ],
  [
    "bullet",
    "Develop internal tools for repetitive tasks; worked on separate employee-management, scheduling and laboratory-process applications."
  ],
  [
    "section",
    "SELECTED PROJECTS"
  ],
  [
    "title",
    "LabFlow | healthcare-related application project"
  ],
  [
    "body",
    "Demonstration laboratory workflow application built with Django and React. Designed process stages, forms, user roles and an audit trail; worked with PostgreSQL/SQLite, validation and testing. Prepared user and technical documentation, including setup and recovery guidance."
  ],
  [
    "body",
    "JobHunter: n8n/PostgreSQL workflow automation with automated tests and GitHub Actions CI. Additional engineering projects: Fusion 360, AutoCAD and RobotStudio."
  ],
  [
    "section",
    "EDUCATION"
  ],
  [
    "title",
    "WSB Merito we Wrocławiu | 03.2026 - present"
  ],
  [
    "body",
    "Network, systems and IT security engineering; part-time engineering studies, second semester."
  ],
  [
    "title",
    "Politechnika Wrocławska | 10.2022 - present"
  ],
  [
    "body",
    "Robotics and Process Automation; engineering studies in progress, five semesters completed."
  ],
  [
    "section",
    "LANGUAGES AND AVAILABILITY"
  ],
  [
    "body",
    "Polish - advanced; English - advanced / technical; Ukrainian and Russian - native. IT Step Python AI course, 02.2024 - 12.2024. Category B driving licence."
  ],
  [
    "body",
    "Seeking flexible working hours. From March 2027: available onsite in Wrocław up to 1-2 days per week, with remaining work remote. Open to part-time arrangements; start date by agreement."
  ]
]


======== FILE: StoryGold_CAD_Evaluation_EN_content.json ========

[
  [
    "name",
    "Denis Gruszkiewicz"
  ],
  [
    "role",
    "CAD Evaluation Engineer | Mechanical design, FEA / CFD and Python / ML"
  ],
  [
    "contact",
    "Wrocław, Poland | +48 511 592 887 | r3dflzp.ns@gmail.com"
  ],
  [
    "contact",
    "GitHub: github.com/Flyingzaptop"
  ],
  [
    "section",
    "PROFILE AND MOTIVATION"
  ],
  [
    "body",
    "Engineering student with hands-on projects in mechanical CAD, centrifugal-force FEA and basic supersonic CFD, complemented by Python/PyTorch research and automated testing. My work includes an axial turbojet engine, a cycloidal drive and a RAMJET prototype project. StoryGold is a top-priority opportunity because it connects this mechanical-design foundation with my experience defining metrics, investigating failures and building repeatable model evaluations."
  ],
  [
    "section",
    "CAD AND ENGINEERING FOUNDATION"
  ],
  [
    "body",
    "Fusion 360: parts and assemblies. AutoCAD: 2D technical documentation. Geometry, assembly relationships, dimensions, fits and tolerances; STEP/STL and FDM-aware design. Basic Siemens NX; academic RobotStudio welding and palletizing cells."
  ],
  [
    "section",
    "SELECTED MECHANICAL DESIGN AND SIMULATION PROJECTS"
  ],
  [
    "title",
    "Axial Turbojet Engine | CAD and centrifugal-force FEA"
  ],
  [
    "body",
    "Developed the engine concept and CAD models of its main components, considering geometry and component arrangement. Used finite element analysis to investigate centrifugal loading within the project, connecting mechanical design with structural analysis."
  ],
  [
    "title",
    "RAMJET Engine Prototype | basic Mach 2+ CFD simulation"
  ],
  [
    "body",
    "Worked on a RAMJET engine prototype project with basic CFD simulation of Mach 2+ flow. Combined design work with an introductory computational investigation of supersonic flow behaviour."
  ],
  [
    "title",
    "Cyclo | cycloidal drive and technical drawing package"
  ],
  [
    "body",
    "Developed mechanical component geometry and an assembly, examining how the parts interact and fit together. Prepared seven drawing sheets: the assembly, input shaft, cycloidal disc, housing, mount, output disc and pin. Documentation includes sections, a parts list, dimensions and selected fits, tolerances and surface-finish symbols."
  ],
  [
    "image",
    "cyclo-fixed.png"
  ],
  [
    "caption",
    "Example from my Cyclo drawing package: assembly sections and component references. The original title block uses my earlier name spelling, Denys Hrushkevych."
  ],
  [
    "body",
    "Contribution to StoryGold: mechanical context for inspecting CAD geometry and constraints, plus Python and testing experience for benchmark tasks, automated scoring and failure analysis. I want to build on this foundation in CAD/CAE evaluation for AI-generated designs."
  ],
  [
    "page",
    ""
  ],
  [
    "section",
    "PYTHON AND MACHINE LEARNING EVALUATION"
  ],
  [
    "title",
    "XAUUSD and stargazin | independent sequence-model research"
  ],
  [
    "bullet",
    "Built Python/PyTorch pipelines for data preparation, feature and target design, model training, checkpointing and scoring; explored TCN, CT-LSTM and RetNet-lite architectures."
  ],
  [
    "bullet",
    "Compared models against baselines, tested chronological validity and data leakage, and investigated unstable predictions and preprocessing inconsistencies. Designed custom losses and evaluation metrics."
  ],
  [
    "contact",
    "github.com/Flyingzaptop/xauusd | github.com/Flyingzaptop/stargazin"
  ],
  [
    "title",
    "GC MBO research | simulation and hypothesis testing"
  ],
  [
    "body",
    "Python feature engineering and model experiments on event-level market data, with Rust replay and conservative FIFO execution simulation. Used walk-forward evaluation, causality checks and cost/latency stress tests. Documented failed hypotheses and limitations to distinguish apparent performance from robust evidence."
  ],
  [
    "contact",
    "github.com/Flyingzaptop/gc-mbo-research"
  ],
  [
    "section",
    "AUTOMATION AND REGRESSION TESTING"
  ],
  [
    "title",
    "ARC - Adaptive Runtime Core | C++ / CMake / CTest / D3D12"
  ],
  [
    "body",
    "Experimental runtime and resource-management research. Worked on automated regression tests and Windows/Linux CI builds across Debug/Release configurations, with GPU/runtime checks. Analysed dependencies, resource behaviour and performance to investigate failures systematically."
  ],
  [
    "title",
    "JobHunter | LLM workflows with deterministic validation"
  ],
  [
    "body",
    "Built an automation platform using n8n, Node.js, PostgreSQL, Ollama, Playwright and Docker. Combined deterministic processing with schema-validated LLM analysis, a React/SSE dashboard, human-in-the-loop controls and GitHub Actions tests. This experience is directly useful when connecting model outputs to repeatable evaluation procedures."
  ],
  [
    "title",
    "LabFlow | application logic, roles and auditability"
  ],
  [
    "body",
    "Django REST Framework and React/TypeScript laboratory workflow demonstrator with user roles, audit history, PostgreSQL/SQLite and validation of application rules. Prepared setup, backup and recovery documentation. Also co-developing Antillia, an early-stage software and automation initiative."
  ],
  [
    "section",
    "PROFESSIONAL EXPERIENCE"
  ],
  [
    "title",
    "Junior IT Administrator | ZOZ w Bolesławcu | 06.2025 - present"
  ],
  [
    "bullet",
    "Provide technical support to hospital staff; diagnose hardware, Windows, connectivity and application issues, reproduce reported defects and verify fixes."
  ],
  [
    "bullet",
    "Translate user needs into internal tools and test application workflows. Worked on separate employee-management, scheduling and laboratory-process applications."
  ],
  [
    "section",
    "EDUCATION AND TECHNICAL FOUNDATION"
  ],
  [
    "body",
    "Politechnika Wrocławska | Robotics and Process Automation | 10.2022 - present. Engineering degree in progress; five semesters completed. Coursework in mechanics, engineering mathematics, physics, machine design, automation and robotics."
  ],
  [
    "body",
    "WSB Merito Wrocław | Network, Systems and IT Security Engineering | 03.2026 - present; part-time studies, second semester. IT Step Python AI course | 02.2024 - 12.2024."
  ],
  [
    "body",
    "Tools: Fusion 360, AutoCAD, basic Siemens NX, RobotStudio; Python, PyTorch, NumPy, Pandas, C++, Git/GitHub, CMake/CTest, PostgreSQL, Django, React and n8n."
  ],
  [
    "section",
    "LANGUAGES AND WORKING ARRANGEMENTS"
  ],
  [
    "body",
    "English - advanced / technical; Polish - advanced; Ukrainian and Russian - native. Seeking remote work with flexible hours compatible with studies. From March 2027, onsite availability is limited to 1-2 days per week in Wrocław. Start date by agreement."
  ]
]


======== FILE: Greenbrier_CV_text_PL.txt ========

Denis Gruszkiewicz

Młodszy Konstruktor | CAD 2D/3D, mechanika i prototypowanie

Wrocław | +48 511 592 887 | r3dflzp.ns@gmail.com

Prawo jazdy kat. B od 3 lat | github.com/Flyingzaptop - projekty IT i R&D

PROFIL ZAWODOWY

Student Robotyki i Automatyzacji Procesów na Politechnice Wrocławskiej, po ukończeniu V semestru. Rozwijam własne projekty mechaniczne i akademickie projekty robotyki, łącząc modelowanie 3D, rysunek techniczny i analizę współpracy elementów. Pracuję przede wszystkim w Fusion 360 i AutoCAD. Chcę wykorzystać tę podstawę na stanowisku Młodszego Konstruktora w Greenbrier, rozwijając umiejętność przygotowywania modeli, rysunków i dokumentacji oraz poznając normy branży kolejowej. Dodatkowym atutem jest doświadczenie zawodowe w diagnozowaniu problemów technicznych i testowaniu aplikacji.

KOMPETENCJE KONSTRUKCYJNE

Fusion 360 - główne środowisko modelowania 3D; części, złożenia i analiza geometrii konstrukcji.

AutoCAD - rysunek 2D i dokumentacja techniczna; interpretacja rysunków oraz przestrzenne rozumienie konstrukcji.

Projektowanie mechanizmów: analiza zasady działania, współpracy elementów, montażu, tolerancji i precyzji wykonania w projektach własnych.

Prototypowanie: modele STEP/STL, przygotowanie elementów do druku 3D i uwzględnianie ograniczeń technologii FDM.

Siemens NX i FluidSim - podstawy; RobotStudio - akademickie stanowiska spawania i paletyzacji.

Podstawy projektowania maszyn, mechaniki, technologii materiałów i procesów obróbki rozwijane w ramach studiów.

WYBRANE PROJEKTY INŻYNIERSKIE

Przekładnia cykloidalna | projekt własny

Projektowanie geometrii przekładni oraz modelowanie części mechanicznych.

Analiza zasady działania i współpracy elementów mechanizmu, z uwzględnieniem montażu, tolerancji oraz praktycznego wykonania.

Osiowy silnik odrzutowy | projekt koncepcyjny

Samodzielne opracowanie koncepcji oraz modelowanie głównych elementów konstrukcyjnych w CAD.

Analiza geometrii, układu przepływu i rozmieszczenia komponentów; wizualizacja rozwiązania technicznego.

RobotStudio | projekty akademickie

Projektowanie stanowisk zrobotyzowanych dla procesów spawania i paletyzacji.

Analiza trajektorii, zasięgu robota, organizacji stanowiska i logiki kolejnych etapów procesu.

Druk 3D i prototypowanie | projekty własne

Projektowanie elementów pod druk 3D i praca z modelami STEP/STL. Uwzględnianie ograniczeń FDM oraz praktyczne podejście do montażu, testowania i poprawiania konstrukcji.

WYKSZTAŁCENIE

Politechnika Wrocławska | 10.2022 - obecnie

Robotyka i Automatyzacja Procesów, studia inżynierskie w toku; ukończony V semestr.

Zakres: mechanika, fizyka techniczna, matematyka inżynierska, rysunek techniczny, CAD, projektowanie maszyn, automatyka i robotyka przemysłowa.

Projekty i zajęcia związane ze stanowiskami zrobotyzowanymi, spawaniem, paletyzacją, obróbką materiałów i symulacją układów.

Uniwersytet WSB Merito we Wrocławiu | 03.2026 - obecnie

Inżynieria sieci, systemów i bezpieczeństwa IT; studia inżynierskie niestacjonarne, II semestr. Rozwijanie kompetencji informatycznych wspierających analizę danych i pracę z systemami technicznymi.

DOŚWIADCZENIE ZAWODOWE

Młodszy Administrator IT | ZOZ w Bolesławcu | 06.2025 - obecnie

Bieżące wsparcie techniczne pracowników oraz diagnozowanie problemów sprzętowych, systemowych i aplikacyjnych.

Analiza potrzeb użytkowników, odtwarzanie błędów i testowanie scenariuszy działania narzędzi.

Rozwój wewnętrznych aplikacji usprawniających pracę: oddzielne projekty zarządzania pracownikami, grafikiem i procesami laboratoryjnymi.

Podłączanie i konfiguracja stanowisk oraz urządzeń sieciowych, okablowanie LAN i podstawowa diagnostyka połączeń.

DODATKOWE PROJEKTY I UMIEJĘTNOŚCI TECHNICZNE

Analiza danych i programowanie

Python, NumPy i Pandas; własne badania danych czasowych i modeli ML. Pozyskiwanie i przygotowanie danych, projektowanie metryk, porównywanie eksperymentów oraz analiza błędów i ograniczeń wyników.

LabFlow i ARC | projekty software / R&D

LabFlow: demonstracyjna aplikacja Django/React odwzorowująca wieloetapowy proces laboratoryjny, z rolami, walidacją i audytem. ARC: eksperymentalny runtime C++/D3D12, analiza zasobów, zależności i wydajności oraz testy. Projekty rozwijają systemowe podejście do problemów i weryfikacji rozwiązań.

Bardzo dobra znajomość Microsoft 365 / MS Office, w tym Excel i PowerPoint. Diagnostyka, składanie i modernizacja komputerów PC, także konfiguracji hard-tube water cooling. Współtworzenie inicjatywy Antillia związanej z aplikacjami i automatyzacją.

KURSY, JĘZYKI I INFORMACJE DODATKOWE

IT Step - Python AI | 02.2024 - 12.2024; kurs programowania w Pythonie i sztucznej inteligencji.

Polski - zaawansowany; angielski - zaawansowany / techniczny; ukraiński i rosyjski - ojczyste.

Prawo jazdy kat. B od 3 lat. Miejsce zamieszkania: Wrocław. Termin rozpoczęcia pracy do uzgodnienia.


======== FILE: Greenbrier_message_PL.txt ========

Szanowni Państwo,

chciałbym zgłosić swoją kandydaturę na stanowisko Młodszego Konstruktora w Greenbrier Poland. Studiuję Robotykę i Automatyzację Procesów na Politechnice Wrocławskiej; ukończyłem V semestr i kontynuuję studia inżynierskie.

Rozwijam własne projekty mechaniczne, korzystając z Fusion 360 i AutoCAD. W załączeniu przesyłam CV oraz przykład mojego projektu przekładni cykloidalnej z rysunkiem złożeniowym i rysunkami wykonawczymi części. Pracując nad nim, zajmowałem się geometrią części, ich współpracą w złożeniu i zagadnieniami montażu.

Zależy mi na rozpoczęciu pracy konstruktorskiej i rozwijaniu umiejętności modelowania 3D oraz przygotowywania dokumentacji technicznej pod opieką doświadczonego zespołu. Jestem gotowy poznawać normy i specyfikę branży kolejowej. Posługuję się angielskim technicznym, bardzo dobrze znam MS Office i posiadam prawo jazdy kat. B.

Będę wdzięczny za rozważenie mojej kandydatury również na obecnym etapie studiów. Chętnie opowiem o projekcie oraz omówię możliwość współpracy.

Z poważaniem,
Denis Gruszkiewicz
+48 511 592 887
r3dflzp.ns@gmail.com

