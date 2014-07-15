var app = angular.module('myApp', []);

app.controller('FilesController', function($scope, $http) {

    $scope.files_left = [];

    $scope.loadFiles = function() {
        var httpRequest = $http({
            method: 'POST',
            url: '/files/list/C:/',
            data: null

        }).success(function(data, status) {
            $scope.files_left = data.files;
            console.log(data);
        });

    };

    $scope.loadFiles();
});