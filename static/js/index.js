/**
 * Created by jwl on 2016/12/1.
 */
var sex_c = $("#sex-canvas");
var sex_canvas = null;
var school_c = $("#school-canvas");
var school_canvas = null;
var nickname_c = $("#nickname-canvas");
var nickname_canvas = null;
var trade_c = $("#trade-canvas");
var trade_canvas = null;
var location_c = $("#location-canvas");
var location_canvas = null;
var company_c = $("#company-canvas");
var company_canvas = null;
var agree_c = $("#agree-canvas");
var agree_canvas = null;
var follower_c = $("#follower-canvas");
var follower_canvas = null;
getData = {
    count: function () {
        var labels = [];
        var nums = [];
        var background = [];
        http.get("/get_count")
            .success(function (result) {
                result = parseJson(result)[0];
                if (result.code == 3) {
                    $("#already_get_num").text(result.data.num);
                    $("#update_time").text(result.data.update_time);
                }
            });
    },
    setSex: function () {
        var labels = [];
        var nums = [];
        var background = [];
        http.get("/get_sex_count")
            .success(function (result) {
                result = parseJson(result)[0];
                if (result.code == 3) {
                    for (key in result.data) {
                        labels.push(key);
                        nums.push(result.data[key]);
                        var color_a = getRandom(0);
                        var color_b = getRandom(0);
                        var color_c = getRandom(0);
                        background.push('rgba(' + color_a + ', ' + color_b + ', ' + color_c + ',0.85)')
                    }
                }
                zhihuChart.sex(labels, nums, background);
            });
    },
    setSchool: function () {
        var labels = [];
        var nums = [];
        var background = [];
        http.get("/get_school_count")
            .success(function (result) {
                result = parseJson(result)[0];
                if (result.code == 3) {
                    for (key in result.data) {
                        labels.push(key);
                        nums.push(result.data[key]);
                        var color_a = getRandom(0);
                        var color_b = getRandom(0);
                        var color_c = getRandom(0);
                        background.push('rgba(' + color_a + ', ' + color_b + ', ' + color_c + ',0.9)')
                    }
                }
                zhihuChart.school(labels, nums, background);
            });
    },
    setNickname: function () {
        var labels = [];
        var nums = [];
        var background = [];
        http.get("/get_nickname_count")
            .success(function (result) {
                result = parseJson(result)[0];
                if (result.code == 3) {
                    for (key in result.data) {
                        labels.push(key);
                        nums.push(result.data[key]);
                        var color_a = getRandom(0);
                        var color_b = getRandom(0);
                        var color_c = getRandom(0);
                        background.push('rgba(' + color_a + ', ' + color_b + ', ' + color_c + ',0.9)')
                    }
                }
                zhihuChart.nickname(labels, nums, background);
            });
    },
    setTrade: function () {
        var labels = [];
        var nums = [];
        var background = [];
        http.get("/get_trade_count")
            .success(function (result) {
                result = parseJson(result)[0];
                if (result.code == 3) {
                    for (key in result.data) {
                        labels.push(key);
                        nums.push(result.data[key]);
                        var color_a = getRandom(0);
                        var color_b = getRandom(0);
                        var color_c = getRandom(0);
                        background.push('rgba(' + color_a + ', ' + color_b + ', ' + color_c + ',0.9)')
                    }
                }
                zhihuChart.trade(labels, nums, background);
            });
    },
    setLocation: function () {
        var labels = [];
        var nums = [];
        var background = [];
        http.get("/get_location_count")
            .success(function (result) {
                result = parseJson(result)[0];
                if (result.code == 3) {
                    for (key in result.data) {
                        labels.push(key);
                        nums.push(result.data[key]);
                        var color_a = getRandom(0);
                        var color_b = getRandom(0);
                        var color_c = getRandom(0);
                        background.push('rgba(' + color_a + ', ' + color_b + ', ' + color_c + ',0.9)')
                    }
                }
                zhihuChart.location(labels, nums, background);
            });
    },
    setCompany: function () {
        var labels = [];
        var nums = [];
        var background = [];
        http.get("/get_company_count")
            .success(function (result) {
                result = parseJson(result)[0];
                if (result.code == 3) {
                    for (key in result.data) {
                        labels.push(key);
                        nums.push(result.data[key]);
                        var color_a = getRandom(0);
                        var color_b = getRandom(0);
                        var color_c = getRandom(0);
                        background.push('rgba(' + color_a + ', ' + color_b + ', ' + color_c + ',0.9)')
                    }
                }
                zhihuChart.company(labels, nums, background);
            });
    },
    setAgree: function () {
        var labels = [];
        var nums = [];
        var background = [];
        http.get("/get_agree_count")
            .success(function (result) {
                result = parseJson(result)[0];
                if (result.code == 3) {
                    for (key in result.data) {
                        labels.push(key);
                        nums.push(result.data[key]);
                        var color_a = getRandom(0);
                        var color_b = getRandom(0);
                        var color_c = getRandom(0);
                        background.push('rgba(' + color_a + ', ' + color_b + ', ' + color_c + ',0.9)')
                    }
                }
                zhihuChart.agree(labels, nums, background);
            });
    },
    setFollower: function () {
        var labels = [];
        var nums = [];
        var background = [];
        http.get("/get_follower_count")
            .success(function (result) {
                result = parseJson(result)[0];
                if (result.code == 3) {
                    for (key in result.data) {
                        labels.push(key);
                        nums.push(result.data[key]);
                        var color_a = getRandom(0);
                        var color_b = getRandom(0);
                        var color_c = getRandom(0);
                        background.push('rgba(' + color_a + ', ' + color_b + ', ' + color_c + ',0.9)')
                    }
                }
                zhihuChart.follower(labels, nums, background);
            });
    },
};

//性别比例初始化


zhihuChart = {

    //设置性别统计
    sex: function (labels, nums, background) {
        var d = {
            labels: labels,
            datasets: [
                {
                    label: '性别比例',
                    data: nums,
                    backgroundColor: background
                }
            ]
        };
        //新建canvas
        sex_canvas = new Chart(sex_c, {
            type: 'pie',
            data: d,
        })
    },
    //学校人群分布统计
    school: function (labels, nums, background) {
        var d = {
            labels: labels,
            datasets: [
                {
                    label: '用户学校分布TOP10',
                    data: nums,
                    backgroundColor: background
                }
            ]
        };
        //新建canvas
        school_canvas = new Chart(school_c, {
            type: 'bar',
            data: d,
        })
    },
    //昵称统计
    nickname: function (labels, nums, background) {
        var d = {
            labels: labels,
            datasets: [
                {
                    label: '最常用名称TOP20',
                    data: nums,
                    backgroundColor: background
                }
            ]
        };
        //新建canvas
        nickname_canvas = new Chart(nickname_c, {
            type: 'bar',
            data: d,
        })
    },
    trade: function (labels, nums, background) {
        var d = {
            labels: labels,
            datasets: [
                {
                    label: '用户行业分布TOP10',
                    data: nums,
                    backgroundColor: background
                }
            ]
        };
        //新建canvas
        trade_canvas = new Chart(trade_c, {
            type: 'bar',
            data: d,
        })
    },
    location: function (labels, nums, background) {
        var d = {
            labels: labels,
            datasets: [
                {
                    label: '用户地区分布TOP10',
                    data: nums,
                    backgroundColor: background
                }
            ]
        };
        //新建canvas
        location_canvas = new Chart(location_c, {
            type: 'bar',
            data: d,
        })
    },
    company: function (labels, nums, background) {
        var d = {
            labels: labels,
            datasets: [
                {
                    label: '用户公司分布TOP10',
                    data: nums,
                    backgroundColor: background
                }
            ]
        };
        //新建canvas
        company_canvas = new Chart(company_c, {
            type: 'bar',
            data: d,
        })
    },
    agree: function (labels, nums, background) {
        var d = {
            labels: labels,
            datasets: [
                {
                    label: '获取赞同数分布',
                    data: nums,
                    backgroundColor: background
                }
            ]
        };
        //新建canvas
        agree_canvas = new Chart(agree_c, {
            type: 'doughnut',
            data: d,
        })
    },
    follower: function (labels, nums, background) {
        var d = {
            labels: labels,
            datasets: [
                {
                    label: '用户粉丝数分布',
                    data: nums,
                    backgroundColor: background
                }
            ]
        };
        //新建canvas
        follower_canvas = new Chart(follower_c, {
            type: 'doughnut',
            data: d
        })
    },

}