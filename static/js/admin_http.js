request = {
    get: function (url,data) {
        return $.ajax({
            type: "GET",
            url: url,
            data: data,
            async: true
        });
    },
    post: function (url,data) {
        return $.ajax({
            type: "POST",
            url: url,
            data: data,
            async: true
        });
    },
    put: function (url,data) {
        return $.ajax({
            type: "PUT",
            url: url,
            data: data,
            async: true
        });
    },
    delete: function (url,data) {
        return $.ajax({
            type: "DELETE",
            url: url,
            data: data,
            async: true
        });
    },
};
