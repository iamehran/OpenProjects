var app = angular.module("myGroceryList", []);

app.controller("myCtrl", function($scope) {

  $scope.products = ["Eggs", "Milk", "Cake","Bread","butter"];
  $scope.addItem = function() {
 $scope.addMe= $scope.addMe.charAt(0).toUpperCase() + $scope.addMe.slice(1).toLowerCase();
      //return $scope.addMe;
    $scope.errortext = "";
    if (!$scope.addMe) {
      return;
    }
    if ($scope.products.indexOf($scope.addMe) == -1) {
      $scope.products.push($scope.addMe);
    } else {
      $scope.errortext = "* The item is already in your grocery list.";
    }
  }
  $scope.removeItem = function(x) {
    $scope.errortext = "";
    $scope.products.splice(x, 1);
  }
});

function mover(x) {
    x.style.backgroundColor = " #ff9933";
    
}


function mout(x) {
   x.style.backgroundColor ="#FFFFFF" ;
}
