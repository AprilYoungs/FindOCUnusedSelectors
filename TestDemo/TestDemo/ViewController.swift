//
//  ViewController.swift
//  TestDemo
//
//  Created by April Yang on 2020/3/27.
//  Copyright © 2020 April Yang. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        let test1 = AYTest()
        test1.age = 20;
        print(test1.age)
        test1.instanceOne(true)
        AYTest.classOne(true)
        
        let test2 = AYTest()
        test2.name = "April";
        print(test2.name)
        test2.instanceOne(true)
        AYTest.classOne(true)
        
    }


}

