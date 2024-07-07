const dragAndDropItems = document.getElementById(
    'items'
);

new Sortable(dragAndDropItems, {
   animation: 350,
   chosenClass: "item-chosen",
   dragClass: "item-drag",
});

