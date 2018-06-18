# worldcup2018-tickets

//I create these scripts to help me to buy tickets in the WorldCup 2018 in last call for the next day match
//I didn't have time to automate everything as I have done in 2014. 
//So I needed to enter the capthas and configure the snippets manually


//First of all when you logged in you have to run the command below in the console browser 
//to enable debug and you can have access to the Angular scope variable
angular.reloadWithDebugInfo();


//The comamand below allows you to reload the availability with out reload the page or wait the 5min timer
angular.element($0).scope().refreshAvailability();


//To get the Json of selected product, try to get when your product is available. 
//Choose the category and product when it available and keep with you
//Remember to open the inspect the element of the region because the browser need to updade the angular code
//1. Get selectedProduct
JSON.stringify(angular.element($0).scope().selectedProduct);

//2. Get product
JSON.stringify(angular.element($0).scope().product);

//3. Get productIndex
angular.element($0).scope().productIndex;

//4. Get category
angular.element($0).scope().category;


//5. Change the arrays and Json in the variables below. 
//This is the snippet that automate the product selection and open the Captcha even if the product isn't available. 
//So if you still trying you will be the first when it get available. 
//The example below is with the first Germany game. I've bought this game, Portugal vs Marroco, Senegal vs Poland, Brazil vs Swiss and Semifinal whith this method on the June 16th 2018 

angular.element($0).scope().product = JSON.parse('{"ProductId":"IMT11","ProductPublicName":"Match 11 - Saudi Arabia v Egypt - Volgograd","ProductTickets":1,"MatchId":11,"MatchStadium":5,"MatchHomeTeamId":"KSA","MatchAwayTeamId":"EGY","MatchDate":"2018-06-25T17:00:00","Round":"A","SO":11,"ProductTypeCode":"IMT","MatchIsClosed":false,"MatchDateNoTime":"25 JUN 2018","RoundName":"Group Matches","availableCategories":6,"categories":[{"PRPProductId":"IMT11","PRPCategoryId":14,"CurrencyCode":"USD","CategoryName":"CAT 1","PRPAmountN":210,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":14,"Availability":2,"CategoryStyleClass":"","AvailabilityText":"Medium","AvailabilityStyleClass":"yellowAvailability","details":{"CategoryId":14,"CategoryName":"CAT 1","CategoryNameOnTicket":"CATEGORY 1","Accessibility":false,"Colour":"225,7,133","SO":14}},{"PRPProductId":"IMT34","PRPCategoryId":15,"CurrencyCode":"USD","CategoryName":"CAT 2","PRPAmountN":165,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":15,"Availability":1,"AvailabilityStyleClass":"lowAvailability","AvailabilityText":"Low","CategoryStyleClass":"","details":{"CategoryId":15,"CategoryName":"CAT 2","CategoryNameOnTicket":"CATEGORY 2","Accessibility":false,"Colour":"26,137,134","SO":15}},{"PRPProductId":"IMT34","PRPCategoryId":14,"CurrencyCode":"USD","CategoryName":"CAT 3","PRPAmountN":105,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":14,"Availability":1,"AvailabilityStyleClass":"lowAvailability","AvailabilityText":"Low","CategoryStyleClass":"","details":{"CategoryId":14,"CategoryName":"CAT 3","CategoryNameOnTicket":"CATEGORY 3","Accessibility":false,"Colour":"142,82,160","SO":14}}],"Stadium":{"StadiumId":11,"StadiumCode":"VLG","StadiumName":"VLG – Volgograd Arena","StadiumCityId":12,"CityName":"VOLGOGRAD"},"incomp":[35,36,33],"validationSummary":{"isProductAvailable":{"isValid":true,"apply":true,"errors":[],"extraData":{}},"isProductCategoryAvailable":{"isValid":false,"apply":true,"errors":[{"ItemId":"IMT34","Message":"This Category is not available."}],"extraData":{"availableCategories":["14","15","16"]}},"isProductCompatible":{"isValid":true,"apply":true,"errors":[],"extraData":{"incompatibleProducts":[]}},"isProductAllowedToMixinTST":{"isValid":true,"apply":true,"errors":[]},"isProductCategoryAllowed":{"isValid":true,"apply":false,"errors":[],"extraData":{"purchasedCategories":[],"allowedDisableCategories":["18","19","20","21","25","37","38"],"notAllowedDisableCategories":[],"notDisableCategoriesIds":["14","15","16","17","56","22","23","24"],"notAllowedDisabledCategoriesForCombination":[[21,25,37,38]]}},"isProductAvailableByMatch":{"isValid":true,"apply":true,"errors":[{"ItemId":"IMT11","Message":"You are allowed to purchase a maximum of (4) Tickets per Match."}],"extraData":{"availability":4,"HHR":[{"catId":14,"availability":4,"purchased":0,"messageError":"You are allowed to purchase a maximum of (4) Tickets per Match."},{"catId":15,"availability":4,"purchased":0,"messageError":"You are allowed to purchase a maximum of (4) Tickets per Match."},{"catId":14,"availability":4,"purchased":0,"messageError":"You are allowed to purchase a maximum of (4) Tickets per Match."}]}},"isProductLimitedTotalNumberOfMatches":{"isValid":true,"apply":true,"errors":[],"extraData":{}},"isProductIncompatibleWithPreviousRequest":{"isValid":true,"apply":true,"errors":[],"extraData":{}}},"validation":{},"isProductValid":true,"isProductCategoryValid":true}');
angular.element($0).scope().productIndex ={PRPProductId: "IMT11", PRPCategoryId: 14, CurrencyCode: "USD", CategoryName: "CAT 3", PRPAmountN: 105};
angular.element($0).scope().category = {Availability:2, AvailabilityStyleClass:"yellowAvailability", AvailabilityText:"Medium",CategoryName:"CAT 3",CategorySortOrder:14,CategoryStyleClass:"",CurrencyCode:"USD",PRPAmountC:0,PRPAmountN:105,PRPCategoryId:14,PRPProductId:"IMT11",ProductTypeCode:"IMT",details:{Accessibility:false,CategoryId:14,CategoryName:"CAT 3",CategoryNameOnTicket:"CATEGORY 3",Colour:"225,7,133",SO:14}};
angular.element($0).scope().setselectedProduct(angular.element($0).scope().productIndex,angular.element($0).scope().product,angular.element($0).scope().category); 
angular.element($0).scope().setselectedProductAmount(3);
angular.element($0).scope().selectedProduct = JSON.parse('{"index":"0IMT11","product":{"ProductId":"IMT11","ProductPublicName":"Match 11 - Germany v Mexico - Moscow Luzhniki","ProductTickets":1,"MatchId":11,"MatchStadium":5,"MatchHomeTeamId":"GER","MatchAwayTeamId":"MEX","MatchDate":"2018-06-17T18:00:00","Round":"A","SO":11,"ProductTypeCode":"IMT","MatchIsClosed":false,"MatchDateNoTime":"17 JUN 2018","RoundName":"Group Matches","availableCategories":1,"categories":[{"PRPProductId":"IMT11","PRPCategoryId":14,"CurrencyCode":"USD","CategoryName":"CAT 1","PRPAmountN":210,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":14,"Availability":0,"CategoryStyleClass":"disabledItem","AvailabilityText":"&nbsp;","AvailabilityStyleClass":"zeroAvailability","details":{"CategoryId":14,"CategoryName":"CAT 1","CategoryNameOnTicket":"CATEGORY 1","Accessibility":false,"Colour":"225,7,133","SO":14}},{"PRPProductId":"IMT11","PRPCategoryId":15,"CurrencyCode":"USD","CategoryName":"CAT 2","PRPAmountN":165,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":15,"Availability":0,"CategoryStyleClass":"disabledItem","AvailabilityText":"&nbsp;","AvailabilityStyleClass":"zeroAvailability","details":{"CategoryId":15,"CategoryName":"CAT 2","CategoryNameOnTicket":"CATEGORY 2","Accessibility":false,"Colour":"26,137,134","SO":15}},{"PRPProductId":"IMT11","PRPCategoryId":14,"CurrencyCode":"USD","CategoryName":"CAT 3","PRPAmountN":105,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":14,"Availability":1,"AvailabilityStyleClass":"lowAvailability","AvailabilityText":"Low","CategoryStyleClass":"","details":{"CategoryId":14,"CategoryName":"CAT 3","CategoryNameOnTicket":"CATEGORY 3","Accessibility":false,"Colour":"142,82,160","SO":14}}],"Stadium":{"StadiumId":5,"StadiumCode":"MLU","StadiumName":"MLU - Luzhniki Stadium","StadiumCityId":2,"CityName":"MOSCOW"},"incomp":[9,10],"validationSummary":{"isProductAvailable":{"isValid":true,"apply":true,"errors":[],"extraData":{}},"isProductCategoryAvailable":{"isValid":true,"apply":true,"errors":[{"ItemId":"IMT11","Message":"This Category is not available."}],"extraData":{"availableCategories":["14"]}},"isProductCompatible":{"isValid":true,"apply":true,"errors":[],"extraData":{"incompatibleProducts":[]}},"isProductAllowedToMixinTST":{"isValid":true,"apply":true,"errors":[]},"isProductCategoryAllowed":{"isValid":true,"apply":false,"errors":[],"extraData":{"purchasedCategories":[],"allowedDisableCategories":["18","19","20","21","25","37","38"],"notAllowedDisableCategories":[],"notDisableCategoriesIds":["14","15","16","17","56","22","23","24"],"notAllowedDisabledCategoriesForCombination":[[21,25,37,38]]}},"isProductAvailableByMatch":{"isValid":true,"apply":true,"errors":[{"ItemId":"IMT11","Message":"You are allowed to purchase a maximum of (4) Tickets per Match."}],"extraData":{"availability":4,"HHR":[{"catId":14,"availability":4,"purchased":0,"messageError":"You are allowed to purchase a maximum of (4) Tickets per Match."},{"catId":15,"availability":4,"purchased":0,"messageError":"You are allowed to purchase a maximum of (4) Tickets per Match."},{"catId":14,"availability":4,"purchased":0,"messageError":"You are allowed to purchase a maximum of (4) Tickets per Match."}]}},"isProductLimitedTotalNumberOfMatches":{"isValid":true,"apply":true,"errors":[],"extraData":{}},"isProductIncompatibleWithPreviousRequest":{"isValid":true,"apply":true,"errors":[],"extraData":{}}},"validation":{},"isProductValid":true,"isProductCategoryValid":true},"category":{"PRPProductId":"IMT11","PRPCategoryId":14,"CurrencyCode":"USD","CategoryName":"CAT 3","PRPAmountN":105,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":14,"Availability":1,"AvailabilityStyleClass":"lowAvailability","AvailabilityText":"Low","CategoryStyleClass":"","details":{"CategoryId":14,"CategoryName":"CAT 3","CategoryNameOnTicket":"CATEGORY 3","Accessibility":false,"Colour":"142,82,160","SO":14}},"amount":3,"Seats":null,"AreConsecutive":null,"maxPurchase":4}');
angular.element($0).scope().addToCart(JSON.parse('{"index":"0IMT11","product":{"ProductId":"IMT11","ProductPublicName":"Match 11 - Germany v Mexico - Moscow Luzhniki","ProductTickets":1,"MatchId":11,"MatchStadium":5,"MatchHomeTeamId":"GER","MatchAwayTeamId":"MEX","MatchDate":"2018-06-17T18:00:00","Round":"A","SO":11,"ProductTypeCode":"IMT","MatchIsClosed":false,"MatchDateNoTime":"17 JUN 2018","RoundName":"Group Matches","availableCategories":1,"categories":[{"PRPProductId":"IMT11","PRPCategoryId":14,"CurrencyCode":"USD","CategoryName":"CAT 1","PRPAmountN":210,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":14,"Availability":0,"CategoryStyleClass":"disabledItem","AvailabilityText":"&nbsp;","AvailabilityStyleClass":"zeroAvailability","details":{"CategoryId":14,"CategoryName":"CAT 1","CategoryNameOnTicket":"CATEGORY 1","Accessibility":false,"Colour":"225,7,133","SO":14}},{"PRPProductId":"IMT11","PRPCategoryId":15,"CurrencyCode":"USD","CategoryName":"CAT 2","PRPAmountN":165,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":15,"Availability":0,"CategoryStyleClass":"disabledItem","AvailabilityText":"&nbsp;","AvailabilityStyleClass":"zeroAvailability","details":{"CategoryId":15,"CategoryName":"CAT 2","CategoryNameOnTicket":"CATEGORY 2","Accessibility":false,"Colour":"26,137,134","SO":15}},{"PRPProductId":"IMT11","PRPCategoryId":14,"CurrencyCode":"USD","CategoryName":"CAT 3","PRPAmountN":105,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":14,"Availability":1,"AvailabilityStyleClass":"lowAvailability","AvailabilityText":"Low","CategoryStyleClass":"","details":{"CategoryId":14,"CategoryName":"CAT 3","CategoryNameOnTicket":"CATEGORY 3","Accessibility":false,"Colour":"142,82,160","SO":14}}],"Stadium":{"StadiumId":5,"StadiumCode":"MLU","StadiumName":"MLU - Luzhniki Stadium","StadiumCityId":2,"CityName":"MOSCOW"},"incomp":[9,10],"validationSummary":{"isProductAvailable":{"isValid":true,"apply":true,"errors":[],"extraData":{}},"isProductCategoryAvailable":{"isValid":true,"apply":true,"errors":[{"ItemId":"IMT11","Message":"This Category is not available."}],"extraData":{"availableCategories":["14"]}},"isProductCompatible":{"isValid":true,"apply":true,"errors":[],"extraData":{"incompatibleProducts":[]}},"isProductAllowedToMixinTST":{"isValid":true,"apply":true,"errors":[]},"isProductCategoryAllowed":{"isValid":true,"apply":false,"errors":[],"extraData":{"purchasedCategories":[],"allowedDisableCategories":["18","19","20","21","25","37","38"],"notAllowedDisableCategories":[],"notDisableCategoriesIds":["14","15","16","17","56","22","23","24"],"notAllowedDisabledCategoriesForCombination":[[21,25,37,38]]}},"isProductAvailableByMatch":{"isValid":true,"apply":true,"errors":[{"ItemId":"IMT11","Message":"You are allowed to purchase a maximum of (4) Tickets per Match."}],"extraData":{"availability":4,"HHR":[{"catId":14,"availability":4,"purchased":0,"messageError":"You are allowed to purchase a maximum of (4) Tickets per Match."},{"catId":15,"availability":4,"purchased":0,"messageError":"You are allowed to purchase a maximum of (4) Tickets per Match."},{"catId":14,"availability":4,"purchased":0,"messageError":"You are allowed to purchase a maximum of (4) Tickets per Match."}]}},"isProductLimitedTotalNumberOfMatches":{"isValid":true,"apply":true,"errors":[],"extraData":{}},"isProductIncompatibleWithPreviousRequest":{"isValid":true,"apply":true,"errors":[],"extraData":{}}},"validation":{},"isProductValid":true,"isProductCategoryValid":true},"category":{"PRPProductId":"IMT11","PRPCategoryId":14,"CurrencyCode":"USD","CategoryName":"CAT 3","PRPAmountN":105,"PRPAmountC":0,"ProductTypeCode":"IMT","CategorySortOrder":14,"Availability":1,"AvailabilityStyleClass":"lowAvailability","AvailabilityText":"Low","CategoryStyleClass":"","details":{"CategoryId":14,"CategoryName":"CAT 3","CategoryNameOnTicket":"CATEGORY 3","Accessibility":false,"Colour":"142,82,160","SO":14}},"amount":3,"Seats":null,"AreConsecutive":null,"maxPurchase":4}'));



//6. If the product is selected in the browser you just need to run the command below that it will 
angular.element($0).scope().addToCart(angular.element($0).scope().selectedProduct);



//7. Automating the tearm of use acceptance and your nationality when you didn't purchase any ticket yet


function page2(){
	document.getElementById('documents').scrollTop = document.getElementById('documents').scrollHeight;
	window.scrollTo(0,document.body.scrollHeight);
	setTimeout(page3, 3000);
}

document.getElementById('thirdparty').scrollTop = window.Height;

document.getElementById('nationalForeignCheck').click();
document.getElementById('foreignCheck').click();
document.getElementsByName('countryOfResidence')[0].value="BRA";
document.getElementsByName('countryOfNationality')[0].value="BRA";

angular.element(document.getElementsByName('countryOfResidence')[0]).scope().individualData.countryOfResidence = 'BRA';
angular.element(document.getElementsByName('countryOfResidence')[0]).scope().individualData.nationality = 'BRA';
angular.element(document.getElementsByName('countryOfResidence')[0]).scope().countryOfResidenceUpdate('BRA')
angular.element(document.getElementsByName('countryOfNationality')[0]).scope().nationalityUpdate('BRA')

document.getElementById('nextButton').click();

setTimeout(page2, 1500);

