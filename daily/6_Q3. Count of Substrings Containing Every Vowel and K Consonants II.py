from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(word)
        vowel_count = Counter()
        consonant_count = 0
        count = 0
        left = 0

        for right in range(n):
            # 添加右邊的字符
            if word[right] in vowels:
                vowel_count[word[right]] += 1
            else:
                consonant_count += 1
            
            # 當窗口大小超過 k 時，移動左指針
            while consonant_count > k:
                if word[left] in vowels:
                    vowel_count[word[left]] -= 1
                    if vowel_count[word[left]] == 0:
                        del vowel_count[word[left]]
                else:
                    consonant_count -= 1
                left += 1
            
            # 如果當前窗口包含所有元音且輔音數量為 k，增加計數
            if len(vowel_count) == 5 and consonant_count == k:
                count += 1

        return count

# 測試
word = "baiidoadceubddcbuuuoeuedebidododaoobauaociecbbaaedueouoaiiddaeiooobcabbiuudceccaubbobacbuuioabiaubuedicccbuudeuoooeaocobdobdbooccdeoaciucddcoieoiuacudoaaboiaiciabaocaaaccidbuaiciocbecubuaiiaeboiecioidiiiiducacbduouaooduaudibcieoibdcdebdicaeocbouooiuiduucbieaaacaodboucbiduadaceiacecccbaiaoadcoeubeiiaibeecuboacobcubduacbuiaobouceuibouaoibeduuaaueidabcoidbiiueeeiaecbbeuecocacubecdiodeoaoeccuibdboboaeuoduuuebcdedaeaubiuddeeiiaoauuiieociadbcidieuuebbdbcciiccdeubudcbecoieeuiauooibabdoooduibeiacdccidiaebaudaiioeeicdbeeaiaidebbdcbuaidcbadaicoocoaaobbobdeieeiiieicoudieaauebaoedbecdbuocoudaeiibiioedaacidadaiiabddcauueibbduueaocdaoeiaeceoiibucieideaauobbudobecbocueaeiieeiacoadiuudcaoeidoeiddaiiiioeeiebdbdubobcbeouideabbeiuabeuobabedddceooocbudceaeoecbeciuuoocaiiuieodeiuuouidboeuioadoboaiaeaeebbcdbcoaadoadciiioiebicaoodouiuibecuuboeaecedeiubududuoiebdoidbiacadudiiieboeduuuiuuaueuoeeabcaeceucacaaeoaubeuoodiucidoidaaddbuaeeaucaiabeebucedddccuaiaubidoduocoeeiiuoieodudoaddbobeidcauaiobbuiccubcibdiaeoaiocedccooauueducbdbabdeodaaaeoieaicbaeibiuoueiieaebiucdaooiabuobiebaoiecoebouueueuieeiciiioeaiideceueobdcbuocaicoaoibooccoudbceaeucocbidouiddubaodeccoocubicbbaciodeeooiabdeuoiuuaoooiboidoodecdbcdbidbaciueibouuuiaidbdueaudeaeeeeiebceduabceedddedabcaobdaidudceaoabebobcdeiceaccecubiducoiadbdaacebiaididbboedouuuiiiiaoaiduaeaboaiaibbeecoccodbeddueacbioeebdeddaocacbdaaoaciaeaeuboidiebauucoebeaiidibaocieaboeadbdueiuueaduceaduadauaceaiucibadeeuaiedaiodbiuddcbcodaoodcoeiuebdiceucaddouoocodbbacdiceoibdaoeooboboobuibbaeiddbeubecacidcdubciaiibbccaecuubboucibaacceicebaccbaocucucbedcedcadcdeoaeeaiubaoacbobuciibcddeaaeeeouaoccacduiidaeuaebbdioieuabeoiuouieedoeciuoicicuudcuuuecbiibadbicoeeciuedcdibciuoeodbecaaadbcoodaububaoueubeadeddoaocceoaeccuduceoudeioicuauoecuaeccuibeiebooaucoiaabeebuecceeocaeccoaadeabueadccuaubdodbbcibuaiooecuceabecacbdecdcbcbddodcecueudecodieibdcoeaidaodbaaububebacciibdbcbeeaeoedbeudoabedoddooebeucoebaaaeiiuceduuueabduibbeddibocbiiiauocadeddciiceuaoaeiudaacidaaudubdobieuaiuoabacdeiadedubuduuauuaoucaaiobeoedbcbcobeebuuouebeboudiaoaoaccoouacaiibecciuabuuaabiocdcioibuioodbbbbdbboauebiodcaaiduuoubbeouaiddbiieuuueoiiudbciiiedaaeuoouiceboaieucaidaeoboabaacadooabedideddccbicuuaiceedddbcbdeuaadbcuacodibudeaeiebuouidbduucabuacuabbceooceouedeibccacbuedieaiieibubeeuodcdbbddoiudaiaducdidecouoicceeeuuuabbabeodcdiiiouddcddaaucdeoacidcbeibioadadicocbeioeoaibuddoccbidaaebacdebuuucadccdoibuduuuodoueabeuioduucbceccbeouicbbabibaddiaidcaododbadoeeobidicubuoaciaudcebioaciboioboideiucodaiducaceuoiodaiacbadaaddooucoieocococaccucdcoiaoacoeiidbeduueaibouaebcbeabaoeudbdoccecoueaiciiebbidcdudiiobaeuidoeaudoabdubooacbbcoeuouibceiaciiduodiecdcicobicuabuoaaaeidauueoiaooueiecbicoiuuudiiuudiedcdibodeeaiuuuccubcocdieaibicoueeucciaaebdbecuuiibuueooebudubuiiuaaobeoeibuuuodcoeoeoiooacabobuciueeaiodoabuauaddcaicobeouebiadeecoocceauocudeceeddadcauicadbdiuiciaaceecuiuacaeaeiecacdbdbicuuoubucddobeoeaeeubdbobibecedbubduaoeboeoodiiuduaccbdiccouocbdbauccbeobocicuuudcdouabuoucecbuiodaadcabocodaedabdoecdebeaudoiibebbbobodouioeeibicbdoibaudobiuaucacuccodeddideaciuaoaeeouadeaiaiaebdaedaoueidiaboieuebuboeieicociiioaciodbibbueedoacoeiioibiecocddoaeuiuaueaouaibcdciaioiucaaeabeudouduioaoccadbcadeeuueiaaiiuoecdbdcoccooebdecceouedcidcoeducicbabuoucdoibicbueicoduaicaoiicubbudaaaiieiecbdaeddocbaiocddoediubiabaudicciaidbbuebuocaabiodeduubedbciaadduebbbaiuodeduuadaidciobacdibeeauueouaaodbcoideooebcbddducaeeobudducubcdcocibebaacbebceuouiucoceoduobicucuaceuoedidbiedaiiibbcocbaeouadoeduaidaedodudiebdubiaubiddbebidddieedcueeoiuabuacaccoauiddaddiddiadduceaauouioedeabbuadiiiooioebaaedauididciobbdiacicueeoabecbdececaecaaidcioddouaobuuucdaidbaueacduiobadidueiioibdacaeadceucdeacucoocudbcaddoioiciddedebeuuuoddibiabdbicudauddouoccdbcodcibiduibaociiueubaduubdcuebdeubueedciocdccecouuuiooicocdauabdedebadabcdedueccbiuidocouoboeaaibbuiioccebeadobaueudeeaaaodiieieoceoibccboubaubbdubcbduebdabboodeicbebicueiecdaiubeoaoaeeecaaeceaaeddceudadeoadiiboacaecuabbbiiioabuiudociceoaubiieueiodadcbouudeiadeuouabbeeodbeeuaodiacadecbcedbbducdcuiiadueudoadeeeaiodoobobidcuubbouadcebcdidebiudbiuucoodbauacbueodcdceebeddceiuaccddoobabeobaiebdobbcbdiabaaidocudbuucbabcodieacuciecciebcucuddbaoabbobubeabiedbbcbouudciccuobaaebcucaiiibdduaooeboauoibbeudduceidodddaeuuiodbeoubecbiudoebiecdebauuebaacdaaoubiaueoacueuccuoaduboubodiudddadbaeeuauudcbeobuaobacdaeaeeeuuiiubaidociucedboouabcbciiocaoaoacaciboiieaoucieiieiciiocduioeeeeaducaiudcaaicebddccbecaodbbdbidbdebbiidbaddecdudadeudubbboaabdaiabbdeaodacbiuccabcidocedicuicucdeoibedocdoieuaabcauaaeaadcdbcoiedbubdbbecbbcicoiaedbuiaadobucoabocaoauubuuccbeeoeoibcdeddeueieabdcicbccuuocbdudcubbueacuaeiucicoccoeaabubbiiieaeooaboabuuicucudoedbbuuoduibueudiocicicbodcabbdecdabcbduobudbdaedeuucouaeiibcbceioeedocoiuieeobaoiiaoaouebdodoacdodabuabbeiioceauoaoeccouiueideaoubbeuieuucaicaaabeucoacdduiibbbcaoeodcauoabibeabdiabbcieuccdoauediuieedoubueucccboeobioaiiuuaoadaeoioaucbccaudubduuooduoedubbieiecaiiioabboobdoouiabucieeedoedaedebieeioudaeoaidudoibdoicbaboeeebuabuieeobcuddabaoeuadaeobaace"

k = 2504
print(Solution().countOfSubstrings(word, k)) 