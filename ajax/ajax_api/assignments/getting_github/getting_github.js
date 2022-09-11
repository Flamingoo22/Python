async function git_info(){
    let gitinfo = await fetch('https://api.github.com/users/adion81');

    let git_json = await gitinfo.json();

    let btn = document.querySelector('#btn');

    btn.replaceChildren();

    let imgTag = document.createElement('img');
    imgTag.setAttribute('src',git_json.avatar_url)
    let hTag = document.createElement('h1')
    hTag.innerText = 'Adrien has '+ git_json.followers +' follwers'

    btn.appendChild(hTag)
    btn.appendChild(imgTag)
}

