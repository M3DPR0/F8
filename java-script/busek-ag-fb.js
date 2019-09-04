/**
 * This script will delete all group members which are displayed in a given page.
 *
 * @author: Nir Geier
 * @author: m7shapan
 *
 * Usage:
 *    Load as many users as you need, then open console and paste this script in teh console.
 *    Once the script finished executing you will be see blank members page, reload the next
 *    page and start the process again.
 *
 *    !!! Important
 *    Sometimes after opening teh confirm dialog the page look "freeze" for a while
 *    Its OK and it takes time to remove all users.
 *
 *    If the page doen not return the members list page after few minutes, refresh the page and execute the script again
 */
var FBClearGroup = function () {

    // Get all the Admins settings buttons
    var memberSettings, removeLinks, timer;

    /**
     * This function will click on all the uses admin settings buttons to add the remove link to the page dom
     */
    function exposeRemoveLinks() {

        memberSettings = Array.prototype.slice.call(document.querySelectorAll("[aria-label='Member Settings']"));
        
        // remove first index to avoid delete current user
        memberSettings.shift();

        // Expose all the remove users links
        memberSettings.forEach(function (item) {
            item.click();
        });

        // continue with the delete flow
        timer = setTimeout(openRemoveDialog, 1000);
    }

    /**
     * This function will display the remove dialog
     */
    function openRemoveDialog() {
        clearTimeout(timer);

        // Grab all the remove links
        removeLinks = Array.prototype.slice.call(document.querySelectorAll("a[data-testid='leave_group']"));

        // Verify that the previous step has completed
        if (removeLinks.length < memberSettings.length) {

            // wait for previous step to complete
            timer = setTimeout(openRemoveDialog, 1000);
        } else {

            // Open all the remove dialog
            removeLinks.forEach(function (item, index) {
                if (index == 0) {
                    return;
                }
                item.click();
            });

            // delete the users
            timer = setTimeout(removeUsers, 1000);
        }
    }

    /**
     * This method will click on the remove user and will remove the user form group
     */
    function removeUsers() {

        // Grab all the confirm buttons
        var confirmButton = Array.prototype.slice.call(document.querySelectorAll('.layerConfirm.uiOverlayButton[type="submit"]'));

        // Verify that the previous step has completed
        if (confirmButton.length < (memberSettings.length - 1)) {
            timer = setTimeout(removeUsers, 1000);
        } else {

            // Click on the remove confirm button
            confirmButton.forEach(function (item) {
                item.click();
            });
        }
    }

    exposeRemoveLinks();

}();
