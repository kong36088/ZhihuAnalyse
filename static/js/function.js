String.prototype.trim = function (char, type) {
    if (char) {
        if (type == 'left') {
            return this.replace(new RegExp('^\\' + char + '+', 'g'), '');
        } else if (type == 'right') {
            return this.replace(new RegExp('\\' + char + '+$', 'g'), '');
        }
        return this.replace(new RegExp('^\\' + char + '+|\\' + char + '+$', 'g'), '');
    }
    return this.replace(/^\s+|\s+$/g, '');
};

function parseJson(json) {
    json = json.trim('[','left');
    json = json.trim(']','right');
    return eval('[' + json + ']');
}

function getRandom(start){
    return parseInt(0) + Math.floor(Math.random() * 255);
}