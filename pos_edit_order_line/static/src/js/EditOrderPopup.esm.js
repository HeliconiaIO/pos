import {Component, useState} from "@odoo/owl";
import {Dialog} from "@web/core/dialog/dialog";
import {usePos} from "@point_of_sale/app/store/pos_hook";
import {EditOrderLineInput} from "./EditOrderLineInput.esm";

export class EditOrderPopup extends Component {
    static template = "EditOrderPopup";
    static components = {Dialog, EditOrderLineInput};

    setup() {
        super.setup();
        this._id = 0;
        this.state = useState({array: this._initialize(this.props.array)});
        this.changes = {};
        this.pos = usePos();
        this.handleChange = this.handleChange.bind(this);
    }
    _nextId() {
        return this._id++;
    }
    _emptyItem() {
        return {
            text: "",
            _id: this._nextId(),
        };
    }
    _initialize(array) {
        if (array.length === 0) return [this._emptyItem()];
        return array.map((item) =>
            Object.assign(
                {},
                {_id: this._nextId()},
                typeof item === "object" ? item : {text: item}
            )
        );
    }
    handleChange({id, changes}) {
        var self = this;
        self.changes[id] = changes;
    }

    async confirm() {
        var allowConfirmChanges = true;
        Object.values(this.changes).forEach((updates) => {
            Object.values(updates).forEach((value) => {
                if (isNaN(value)) {
                    allowConfirmChanges = false;
                }
            });
        });
        if (allowConfirmChanges) {
            this.apply_changes(this.changes);
            this.props.close();
        }
    }
    async apply_changes(payload) {
        var order = this.pos.get_order();
        Object.entries(payload).forEach(([id, changes]) => {
            var line = order.get_orderline(id);
            Object.entries(changes).forEach(([key, value]) => {
                if (key === "quantity") {
                    line.set_quantity(value);
                } else if (key === "price") {
                    line.set_unit_price(value);
                } else if (key === "discount") {
                    line.set_discount(value);
                }
            });
        });
    }
}
