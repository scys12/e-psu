const radioButton = document.getElementsByName('is_approve');
const alasanDitolak = document.getElementsByName('alasan_ditolak')[0];

radioButton.forEach( (choice) => {
    choice.addEventListener('change', () => {
        const checkedButton = document.querySelector('input[name="is_approve"]:checked');
        if (checkedButton.value === 'True') {
            alasanDitolak.value='';
            inputParent = alasanDitolak.parentNode.parentNode;
            inputParent.style.visibility = 'hidden';
            alasanDitolak.required = false;
            inputParent.style.opacity = 0;
            inputParent.style.transition = 'visibility 600ms, opacity 200ms linear';
            setTimeout(() => {
                inputParent.style.display = 'none';
            }, 250);
        }else{
            inputParent = alasanDitolak.parentNode.parentNode;
            inputParent.style.display = 'inherit';
            alasanDitolak.required = true;
            setTimeout(() => {
                inputParent.style.opacity = 1;
                inputParent.style.visibility = 'inherit';
            }, 200);            
        }

    });
})