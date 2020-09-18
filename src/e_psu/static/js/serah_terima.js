const addFileStatusButton = document.getElementsByClassName('add-file-status_pengelolaan')[0];
const addTextStatusButton = document.getElementsByClassName('add-text-status_pengelolaan')[0];
const addFileRegulasiButton = document.getElementsByClassName('add-file-regulasi_pemanfaatan_psu')[0];
const addTextRegulasiButton = document.getElementsByClassName('add-text-regulasi_pemanfaatan_psu')[0];
const addFilePolaButton = document.getElementsByClassName('add-file-pola_pengelolaan')[0];
const addTextPolaButton = document.getElementsByClassName('add-text-pola_pengelolaan')[0];

addCancelButton = (className, cancelButton) =>{
    let button = document.createElement("button");
    button.className = `${className}-remove-button btn btn-danger`;
    button.innerHTML = "X";
    button.addEventListener("click", removeFormWithCancelButton.bind(this, cancelButton, className));
    return button
}

createFormText = (formData) => {
    let formText = document.createElement("input");
    formText.className = "textinput textInput form-control";
    formText.id = `id_${formData[0]}_text`;
    formText.name = `${formData[0]}_text`;
    formText.type = "text";
    formText.placeholder = formData[1];
    formText.required = true;
    formText.setAttribute("maxlength", "100")
    return formText;
}

addTextForm = (formData, e) =>{
    e.preventDefault();
    container = addContainerFormGroupWithLabel(`group-${formData[0]}_text`, "Teks")
    const inputGroup = document.createElement("div")
    inputGroup.className = "input-group mb-3"
    
    const formText = createFormText(formData)
    formParent = e.srcElement.parentNode.parentNode;

    const cancelButtonGroup = document.createElement("div")
    cancelButtonGroup.className = "input-group-append";
    cancelButton = addCancelButton(`${formData[0]}`,e.srcElement);
    cancelButtonGroup.appendChild(cancelButton);

    inputGroup.appendChild(formText)
    inputGroup.appendChild(cancelButtonGroup);
    container.appendChild(inputGroup);
    
    setTimeout(() => {
        formParent.appendChild(container);
    },300);

    clickedButton = e.srcElement;
    clickedButton.style.transition = "visibility 0s 2s, opacity 2s linear"
    setTimeout(() => {
        clickedButton.remove()
    },300);
}

addContainerFormGroupWithLabel = (groupName, labelName) => {
    const containerFormGroup = document.createElement("div");
    containerFormGroup.id = groupName;

    const label = document.createElement("label");
    label.style = "font-size:16px;font-weigth:600";
    label.innerHTML = labelName;
    containerFormGroup.appendChild(label)
    return containerFormGroup
}

createFormFile = (fieldName) => {
    const formFile = document.createElement("input");
    formFile.type = "file";
    formFile.className = "dokumenclearablefileinput form-control-file";
    formFile.id = `id_${fieldName}`;
    formFile.name = fieldName;
    formFile.style = "margin-bottom: 15px; margin-top: 15px;background-color: #f6f6f6;padding: 4px;"
    formFile.required = true;
    formFile.accept = "application/pdf";

    return formFile
}

addFileForm = (className, e) =>{
    e.preventDefault();

    containerFormGroup = addContainerFormGroupWithLabel(`group-${className}`, "File")
    const inputGroup = document.createElement("div")
    inputGroup.className = "input-group mb-3"

    const containerFile = document.createElement("div")
    containerFile.className = "custom-file"
    formFile = createFormFile(`${className}`)
    containerFile.appendChild(formFile)

    
    const cancelButtonGroup = document.createElement("div")
    cancelButtonGroup.className = "input-group-append"
    cancelButton = addCancelButton(`${className}`, e.srcElement);
    cancelButtonGroup.appendChild(cancelButton)

    inputGroup.appendChild(containerFile)
    inputGroup.appendChild(cancelButtonGroup)
    containerFormGroup.appendChild(inputGroup)

    formParent = e.srcElement.parentNode.parentNode;
    setTimeout(() => {
        formParent.appendChild(containerFormGroup);
    },300);

    clickedButton = e.srcElement;
    clickedButton.style.transition = "visibility 0s 2s, opacity 2s linear"
    setTimeout(() => {
        clickedButton.remove()
    },300);
}

removeFormWithCancelButton = (button, className,e) =>{
    formParent = e.srcElement.parentNode.parentNode.parentNode.parentNode;
    setTimeout(() => {
        formParent.removeChild(e.srcElement.parentNode.parentNode.parentNode)
    },100);
    buttonDynamicContainer = formParent.querySelectorAll(`[id*="dynamic-button-${className}"`)[0]
    setTimeout(() => {
        buttonDynamicContainer.appendChild(button)
    },200);
}

addTextStatusButton.addEventListener("click", addTextForm.bind(this, ["status_pengelolaan", "Status Pengelolaan"]));
addFileStatusButton.addEventListener("click", addFileForm.bind(this, "status_pengelolaan"));
addTextRegulasiButton.addEventListener("click", addTextForm.bind(this, ["regulasi_pemanfaatan_psu", "Regulasi Pemanfaatan PSU"]));
addFileRegulasiButton.addEventListener("click", addFileForm.bind(this, "regulasi_pemanfaatan_psu"));
addTextPolaButton.addEventListener("click", addTextForm.bind(this, ["pola_pengelolaan", "Pola Pengelolaan"]));
addFilePolaButton.addEventListener("click", addFileForm.bind(this, "pola_pengelolaan"));