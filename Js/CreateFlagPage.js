function createPage(nameFlag) {
    var back = document.createElement('a');
    back.className = 'back';
    back.href = 'List.html';
    back.innerHTML = '<i class="fa fa-chevron-circle-left" aria-hidden="true"></i> Retour';

    var country = document.createElement('div');
    country.className = 'country';

    var countryWrite = document.createElement('div');
    countryWrite.className = 'countryWrite';
    

    var countryName = document.createElement('div');
    countryName.className = 'countryName';
    countryName.innerHTML = nameFlag;

    var countryContent = document.createElement('div');
    countryContent.className = 'countryContent';
    countryContent.innerHTML = getDescription(nameFlag)
    
    countryWrite.appendChild(countryName)
    countryWrite.appendChild(countryContent)
    var blank = document.createElement('div');
    blank.innerHTML = '<br>'

    var img = document.createElement('img');
    nameFlag2 = nameFlag.replace("d'I", 'dI')
    img.src = "http://localhost:8000/" + nameFlag2.replaceAll(' ', '_');
    img.className = 'flagImg'

    var border = document.createElement('div');
    border.className = 'borderImg';
    border.appendChild(img)
    var countryImg = document.createElement('div');
    countryImg.className = 'countryImg';
    
    countryImg.appendChild(blank);
    countryImg.appendChild(border);

    country.appendChild(countryWrite);
    country.appendChild(countryImg);

    var content = document.getElementById('content');
    content.removeChild(document.getElementById('contentHead'))
    content.removeChild(document.getElementById('countryList'))
    content.appendChild(back);
    content.appendChild(country);
}